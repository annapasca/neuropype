.. _cinq:

CINQ
====


Download scripts
----------------

.. code-block:: bash

    git clone https://github.com/davidmeunier79/neuropype_workshop.git
    cd source_code

Upgrade neuropype_ephy
----------------------
 
Go to the directory where you installed neuropype_ephy 
 
.. code-block:: bash

    git checkout dev
    git pull origin dev
    
**Before** to run the scripts set ``main_path`` in ``params.py`` file to the folder where you downloaded the Omega sample datasets

Preprocessing 
-------------

This analysis is based on :ref:`preproc_meeg` Section. The aim is to perform an automatic
removal of eyes and heart related artifacts by applying an ICA algorithm to the raw MEG data. 
One of the output files will be a report that should be used to correct and/or fine-tune the correction in each subject.

Before to run the script ``run_preprocess_pipeline.py``

* look at the variables you can set in ``params_ica.py`` (see :ref:`preproc_example` for more details on the variables)
* set the number of processors ``n_procs`` in

.. code-block:: python
    :emphasize-lines: 1
    
    main_workflow.run(plugin='MultiProc', plugin_args={'n_procs': 3})

* run the script by the command 

.. code-block:: bash
   
    python run_preprocess_pipeline.py

* look at the workflow directory ``preprocessing_pipeline`` created in the ``main_path``
* open ``ipynb_report.ipynb`` running a jupyter notebook

.. code-block:: bash
    
    jupyter notebook 
    
* inspect the report file and save the raw data file in the subject directory


Power analysis
--------------

This analysis is based on :ref:`power` Section to compute the power spectral density (PSD) on the cleaned raw data
on sensor space. 

Before to run the script ``run_power.py``

* look at the variables you can set in ``params_power.py`` (see :ref:`power_example` for more details on the variables)
* set the number of processors ``n_procs`` in

.. code-block:: python
    :emphasize-lines: 1
    
    main_workflow.run(plugin='MultiProc', plugin_args={'n_procs': 3})

* run the script by the command 

.. code-block:: bash
   
    python run_power.py

* look at the workflow directory ``power_pipeline`` created in the ``main_path``
* open ``ipynb_plot_psd.ipynb`` running a jupyter notebook

.. code-block:: bash
    
    jupyter notebook 


Connectivity and graph analysis
-------------------------------

This analysis is based on :ref:`spectral_connectivity` Section

* look at the variables you can set in ``params_conn.py`` (see :ref:`conn_graph_example` for more details on the variables)
* run the script by the command 

.. code-block:: bash
   
    python run_spectral.py

.. seealso:: see :ref:`example` Section for more details on the pipelines