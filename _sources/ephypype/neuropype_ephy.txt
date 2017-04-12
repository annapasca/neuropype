.. _ephypype:

ephypype
********

The ephypype package includes pipelines for electrophysiology analysis.
It's based mainly on MNE-Python package, as well as more standard python libraries such as Numpy and Scipy.
Current implementations allow for 

* MEG/EEG data import
* MEG/EEG data pre-processing and cleaning by an automatic removal of eyes and heart related artifacts
* sensor or source-level connectivity analyses

The ephypype package provides the main pipelines in the :ref:`pipelines`:

* the :ref:`preproc_meeg` runs the ICA algorithm for an automatic removal of eyes and heart related artefacts
* the :ref:`source_reconstruction` computes the inverse solution starting from raw/epoched data
* the :ref:`spectral_connectivity` perform connectivity analysis in sensor or source space

Subpackages
===========

.. toctree::
   :titlesonly:

   
   neuropype_ephy.interfaces
   neuropype_ephy.nodes
   neuropype_ephy.pipelines

