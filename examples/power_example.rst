.. _power_example:

PSD Workflow
============

The following script implements a power pipeline to compute **PSD** on MEG data in **fif** format 
(see :ref:`power` Section). 

Before to run the script, the :ref:`params` should be downloaded (see download
link below). The main **parameters** to set for the power pipeline are
 
* ``main_path`` : main path of the pipeline (*mandatory*) 
* ``fmin`` : min frequency of interest
* ``fmax`` : max frequency of interest
* ``power_method`` : possible choices are *welch* and *multitaper*. If *welch* the power spectral density (PSD) is computed by Welch's method; otherwise it is computed by multitapers
* ``is_epoched`` : *True* if the input data are in epoch format (-epo.fif), *False* if the input data are raw data (-raw.fif)
    
Furthermore, the following **inputnode** must be specified:

* ``fif_file`` : path to raw or epoched MEG data in **fif** format (*mandatory*)

.. seealso:: see :py:func:`create_pipeline_power <neuropype_ephy.pipelines.power.create_pipeline_power>` for a list of all possible inputs

.. code:: python

  import nipype.pipeline.engine as pe
  from nipype.interfaces.utility import IdentityInterface
  import nipype.interfaces.io as nio

  from neuropype_ephy.pipelines.power import create_pipeline_power

  from params_power import main_path, data_path
  from params_power import subject_ids, sessions
  from params_power import power_analysis_name
  from params_power import fmin, fmax, power_method, is_epoched


  def create_infosource():
      """Create node which passes input filenames to DataGrabber"""

      infosource = pe.Node(interface=IdentityInterface(fields=['subject_id',
							      'sess_index']),
			  name="infosource")

      infosource.iterables = [('subject_id', subject_ids),
				  ('sess_index', sessions)]

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


  def create_main_workflow_power():

      main_workflow = pe.Workflow(name=power_analysis_name)
      main_workflow.base_dir = main_path

      # info source
      infosource = create_infosource()

      # data source
      datasource = create_datasource()

      main_workflow.connect(infosource, 'subject_id', datasource, 'subject_id')
      main_workflow.connect(infosource, 'sess_index', datasource, 'sess_index')

      power_workflow = create_pipeline_power(main_path,
					    fmin=fmin, fmax=fmax,
					    method=power_method,
					    is_epoched=is_epoched)

      main_workflow.connect(datasource, 'raw_file',
			    power_workflow, 'inputnode.fif_file')

      return main_workflow


  if __name__ == '__main__':

      # run pipeline:
      main_workflow = create_main_workflow_power()

      main_workflow.write_graph(graph2use='colored')  # colored
      main_workflow.config['execution'] = {'remove_unnecessary_outputs': 'false'}

      main_workflow.run(plugin='MultiProc', plugin_args={'n_procs': 8})

.. _download_power:      

**Download** Parameters file: :download:`params_power.py <../../examples/params_power.py>`

**Download** Python source code: :download:`run_power_analysis.py <../../examples/run_power_analysis.py>`