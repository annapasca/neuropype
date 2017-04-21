"""Workflow for data preprocessing with neuropyconn
OUTLINE:
    import raw .ds data
            ||
            \/
    convert to .fif
            ||
            \/
    filter and downsample
            ||
            \/
    compute ICA solution

CREATED:
    Thu Apr 6 12:32:10 MSK 2017
AUTHOR:
    dmalt

"""

import nipype.pipeline.engine as pe
import nipype.interfaces.io as nio

from nipype.interfaces.utility import IdentityInterface

from neuropype_ephy.pipelines.preproc_meeg import create_pipeline_preproc_meeg

from params import main_path, data_path, subject_ids, sessions
from params import preproc_pipeline_name
from params import data_type, down_sfreq, l_freq, h_freq
from params import variance, ECG_ch_name, EoG_ch_name
from params import is_set_ICA_components, n_comp_exclude


def create_infosource():
    """Create node which passes input filenames to DataGrabber"""
    
    from params import test

    infosource = pe.Node(interface=IdentityInterface(fields=['subject_id',
                                                             'sess_index']),
                         name="infosource")

    if test is False:
        infosource.iterables = [('subject_id', subject_ids),
                                ('sess_index', sessions)]

    else:
        # TEST
        print '*** TEST ***'

        infosource.iterables = [('subject_id', ['sub-0002']),
                                ('sess_index', ['ses-0001'])]

    return infosource


# it could be ds or fif file. Set data_type in the params.py file
def create_datasource():
    """"Create node to grab data"""
    
    from params import test
    
    datasource = pe.Node(interface=nio.DataGrabber(infields=['subject_id',
                                                             'sess_index'],
                                                   outfields=['raw_file']),
                         name='datasource')

    datasource.inputs.base_directory = data_path
    if test:
      datasource.inputs.template = '*%s/%s/meg/%s*rest*short_raw.fif'
    else:
      datasource.inputs.template = '*%s/%s/meg/%s*rest*.ds'
      
    datasource.inputs.template_args = dict(raw_file=[['subject_id',
                                                      'sess_index',
                                                      'subject_id']])

    datasource.inputs.sort_filelist = True

    return datasource


def create_workflow_preproc():
    """Create nodes and connect them into a workflow"""
    
    main_workflow = pe.Workflow(name=preproc_pipeline_name)
    main_workflow.base_dir = main_path

    # Info source
    infosource = create_infosource()

    # Data source
    datasource = create_datasource()

    main_workflow.connect(infosource, 'subject_id', datasource, 'subject_id')
    main_workflow.connect(infosource, 'sess_index', datasource, 'sess_index')

    preproc_workflow = create_pipeline_preproc_meeg(main_path,
                                                    l_freq=l_freq,
                                                    h_freq=h_freq,
                                                    down_sfreq=down_sfreq,
                                                    variance=variance,
                                                    ECG_ch_name=ECG_ch_name,
                                                    EoG_ch_name=EoG_ch_name,
                                                    data_type=data_type,
                                                    is_set_ICA_components=is_set_ICA_components,
                                                    n_comp_exclude=n_comp_exclude)

    main_workflow.connect(infosource, 'subject_id',
                          preproc_workflow, 'inputnode.subject_id')

    main_workflow.connect(datasource, 'raw_file',
                          preproc_workflow, 'inputnode.raw_file')

    return main_workflow


if __name__ == '__main__':

    from params import test

    # run pipeline:
    main_workflow = create_workflow_preproc()

    main_workflow.write_graph(graph2use='colored')  # colored
    main_workflow.config['execution'] = {'remove_unnecessary_outputs': 'false'}

    # Run workflow locally on 2 CPUs
    if test:
        main_workflow.run()
    else:
        main_workflow.run(plugin='MultiProc', plugin_args={'n_procs': 8})
