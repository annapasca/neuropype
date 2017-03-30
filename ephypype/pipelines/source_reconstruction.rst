.. _source_reconstruction:

Source reconstruction pipeline
==============================

The inverse solution pipeline allows to perform source reconstruction starting either from raw/epoched data 
specified by the user or from the output of the :ref:`preproc_meeg` (cleaned raw data).

The output is the source reconstruction matrix that can be used as input of the :ref:`spectral_connectivity`.

The pipeline is defined by the function :py:func:`create_pipeline_source_reconstruction <neuropype_ephy.pipelines.fif_to_inv_sol.create_pipeline_source_reconstruction>`

The three Nodes of the inverse solution pipeline (:py:class:`LF_computation <neuropype_ephy.interfaces.mne.LF_computation>`, 
:py:class:`create_noise_cov <neuropype_ephy.interfaces.mne.Inverse_solution.NoiseCovariance>`, 
:py:class:`inv_solution <neuropype_ephy.interfaces.mne.Inverse_solution>`) 
wrap the MNE Python functions that perform the source reconstruction steps.

In particular:
   
* :ref:`LF_computation`: compute the Lead Field matrix
* :ref:`noise_covariance`: compute the noise covariance matrix
* :ref:`inv_solution`: estimate the time series of the neural sources on a set of dipoles grid

.. _inv_pipeline:

.. figure::  ../../img/graph_dot_inv.jpg
   :scale: 75 %
   :align: center
   
Before to use this pipeline, we need for each subject a template MRI or the individual MRI data.

.. toctree::
   :maxdepth: 1

   nodes/inv_solution