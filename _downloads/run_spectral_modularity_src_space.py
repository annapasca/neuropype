# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:22:47 2016

@author: pasca
"""

import nipype.pipeline.engine as pe
import nipype.interfaces.io as nio

from nipype.interfaces.utility import IdentityInterface

from neuropype_ephy.preproc import get_raw_sfreq
from neuropype_ephy.pipelines.fif_to_inv_sol import create_pipeline_source_reconstruction
from neuropype_ephy.pipelines.ts_to_conmat import create_pipeline_time_series_to_spectral_connectivity

from neuropype_graph.pipelines.conmat_to_graph import create_pipeline_conmat_to_graph_density

from params_src import main_path, data_path, subject_ids, sessions
from params_src import freq_band_names, con_method
from params_src import epoch_window_length, src_correl_analysis_name
from params_src import sbj_dir, spacing, inv_method, parc, aseg, aseg_labels
from params_src import noise_cov_fname
from params_src import mod, con_den


if mod:
    from params_src import radatools_optim


def get_freq_band(freq_band_name):

    from params_src import freq_band_names, freq_bands

    if freq_band_name in freq_band_names:
        print freq_band_name
        print freq_band_names.index(freq_band_name)

        return freq_bands[freq_band_names.index(freq_band_name)]


def create_infosource():

    infosource = pe.Node(interface=IdentityInterface(fields=['subject_id',
                                                             'sess_index',
                                                             'freq_band_name']),
                         name="infosource")


    infosource.iterables = [('subject_id', subject_ids),
			    ('sess_index', sessions),
			    ('freq_band_name', freq_band_names)]

    return infosource


def create_datasource():

    datasource = pe.Node(interface=nio.DataGrabber(infields=['subject_id',
                                                             'sess_index'],
                                                   outfields=['raw_file']),
                         name='datasource')

    datasource.inputs.base_directory = data_path
    datasource.inputs.template = '*%s/%s/meg/%s*rest*ica.fif'
    datasource.inputs.template_args = dict(raw_file=[['subject_id',
                                                      'sess_index',
                                                      'subject_id']])

    datasource.inputs.sort_filelist = True

    return datasource


def create_main_workflow_spectral_modularity_src_space():

    main_workflow = pe.Workflow(name=src_correl_analysis_name)
    main_workflow.base_dir = main_path

    # info source
    infosource = create_infosource()

    # data source
    datasource = create_datasource()

    main_workflow.connect(infosource, 'subject_id', datasource, 'subject_id')
    main_workflow.connect(infosource, 'sess_index', datasource, 'sess_index')

    inv_sol_workflow = create_pipeline_source_reconstruction(main_path,
                                                             sbj_dir,
                                                             spacing=spacing,
                                                             inv_method=inv_method,
                                                             parc=parc,
                                                             aseg=aseg,
                                                             aseg_labels=aseg_labels,
                                                             noise_cov_fname=noise_cov_fname)

    main_workflow.connect(infosource, 'subject_id',
                          inv_sol_workflow, 'inputnode.sbj_id')

    main_workflow.connect(datasource, 'raw_file',
                          inv_sol_workflow, 'inputnode.raw')

    spectral_workflow = \
        create_pipeline_time_series_to_spectral_connectivity(main_path,
                                                             con_method=con_method,
                                                             epoch_window_length=epoch_window_length)
    
    main_workflow.connect(inv_sol_workflow, 'inv_solution.ts_file',
                          spectral_workflow, 'inputnode.ts_file')

    main_workflow.connect(inv_sol_workflow, 'inv_solution.labels',
                          spectral_workflow, 'inputnode.labels_file')

    main_workflow.connect(infosource, ('freq_band_name', get_freq_band),
                          spectral_workflow, 'inputnode.freq_band')

    main_workflow.connect(datasource, ('raw_file', get_raw_sfreq),
                          spectral_workflow, 'inputnode.sfreq')


    graph_den_pipe = create_pipeline_conmat_to_graph_density(main_path,
                                                             con_den=con_den,
                                                             mod=mod,
                                                             plot=True)

    main_workflow.connect(spectral_workflow, 'spectral.conmat_file',
                          graph_den_pipe, 'inputnode.conmat_file')

    if mod:
        graph_den_pipe.inputs.community_rada.optim_seq = radatools_optim

        main_workflow.connect(inv_sol_workflow, 'inv_solution.label_names',
                              graph_den_pipe, 'inputnode.labels_file')
        main_workflow.connect(inv_sol_workflow, 'inv_solution.label_coords',
                              graph_den_pipe, 'inputnode.coords_file')

    return main_workflow


if __name__ == '__main__':

    # run pipeline:
    main_workflow = create_main_workflow_spectral_modularity_src_space()

    main_workflow.write_graph(graph2use='colored')  # colored
    main_workflow.config['execution'] = {'remove_unnecessary_outputs': 'false'}

    main_workflow.run(plugin='MultiProc', plugin_args={'n_procs': 8})
