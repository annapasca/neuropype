.. _params:

params file
===========

We use a parameters file where we define all the variables that are specific for the data analysis.
Here a list of all possible variables for the different pipelines provided by NeuroPype.

Set path and subjects list
++++++++++++++++++++++++++

Set the main directories where the data are stored, the list of subjects and sessions
and the kind of MEG data (ds or fif format)

.. code:: python
    
    import os
  
    data_type = 'ds'
    
    main_path = '/meg_data/omega/sample_BIDS_omega/'
    data_path = main_path
  
    subject_ids = ['sub-0002', 'sub-0003', 'sub-0004', 'sub-0006', 'sub-0007']       
    sessions = ['ses-0001']


Filter parameters
+++++++++++++++++

.. code:: python

    down_sfreq = 800  # sampling frequency at which downsample the data
    l_freq = 0.1
    h_freq = 150


ICA variables
+++++++++++++

Set ``is_ICA = True`` to apply ICA to automatically remove ECG and EoG artifacts

.. code:: python

    is_ICA = True

    # specify ECG and EoG channel names if we have these channels in the data
    # otherwise leave an empty string
    ECG_ch_name = 'ECG'
    EoG_ch_name = 'HEOG, VEOG'
    variance = 0.95

    reject = dict(mag=5e-12, grad=5000e-13)

    # pipeline directory within the main_path dir
    preproc_pipeline_name = "preprocessing_pipeline"

PSD variables
+++++++++++++

.. code:: python

  data_type = 'fif'

  fmin = 0
  fmax = 300
  power_method = 'welch'
  is_epoched = False

  # pipeline directory within the main_path dir
  power_analysis_name = 'power_pipeline'
   
Connectivity variables
++++++++++++++++++++++

Here we specify the frequency bands in which we want to compute the connectivity matrices and the connectivity measure

.. code:: python

    freq_bands = [[2,4], [5,7], [8, 12], [13, 29], [30, 59], [60, 90]]
    freq_band_names = ['delta', 'theta', 'alpha', 'beta', 'gamma1', 'gamma2']
    
    # 'pli', 'plv', 'pli2_unbiased', 'coh', 'cohy', 'ppc', 'wpli', 'wpli2_debiased', 'correl'
    con_method = 'imcoh'
    epoch_window_length = 3.0

    # pipeline directory within the main_path dir
    correl_analysis_name = 'spectral_connectivity_' + data_type + \
				'_' + con_method
    
    
**Download** the parameters file

  * with all variables :download:`params.py  <../../examples/params.py>`
  * for :ref:`preproc_example` example :download:`params_ica.py  <../../examples/params_ica.py>`
  * for :ref:`power_example` example :download:`params_power.py  <../../examples/params_power.py>`
  * for :ref:`conn_graph_example` example :download:`params_power.py  <../../examples/params_congraph.py>`
 