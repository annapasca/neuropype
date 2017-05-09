.. _neuropype_ephy:

neuropype_ephy
**************

The neuropype_ephy package includes pipelines for electrophysiology analysis.
It's based mainly on MNE-Python package, as well as more standard python libraries such as Numpy and Scipy.
Current implementations allow for 

* MEG/EEG data import
* MEG/EEG data pre-processing and cleaning by an automatic removal of eyes and heart related artifacts
* sensor or source-level connectivity analyses

The neuropype_ephy package provides the main pipelines in the :ref:`pipelines`:

* the :ref:`preproc_meeg` runs the ICA algorithm for an automatic removal of eyes and heart related artefacts
* the :ref:`power` computes the power spectral density (PSD) on sensor space
* the :ref:`source_reconstruction` computes the inverse solution starting from raw/epoched data
* the :ref:`spectral_connectivity` perform connectivity analysis in sensor or source space


Pipelines
=========

.. toctree::
   :maxdepth: 3

   pipelines/preproc_meeg
   pipelines/power
   pipelines/source_reconstruction
   pipelines/spectral_connectivity
   

Installation
============

.. toctree::
   :maxdepth: 1

   includeme
   
Subpackages
-----------

.. toctree::
   :maxdepth: 1

   neuropype_ephy.interfaces
   neuropype_ephy.nodes
   neuropype_ephy.pipelines


Modules
-------

neuropype_ephy.aux_tools
------------------------
.. automodule:: neuropype_ephy.aux_tools
    :members:


neuropype_ephy.compute_fwd_problem
----------------------------------

.. automodule:: neuropype_ephy.compute_fwd_problem
    :members:


neuropype_ephy.compute_inv_problem
----------------------------------

.. automodule:: neuropype_ephy.compute_inv_problem
    :members:


neuropype_ephy.fif2ts
---------------------

.. automodule:: neuropype_ephy.fif2ts
    :members:


neuropype_ephy.import_ctf
-------------------------


.. automodule:: neuropype_ephy.import_ctf
    :members:
    

neuropype_ephy.import_mat
-------------------------

.. automodule:: neuropype_ephy.import_mat
    :members:
    

neuropype_ephy.import_txt
-------------------------

.. automodule:: neuropype_ephy.import_txt
    :members:
    

neuropype_ephy.power
--------------------

.. automodule:: neuropype_ephy.power
    :members:
    

neuropype_ephy.preproc
----------------------

.. automodule:: neuropype_ephy.preproc
    :members:


neuropype_ephy.spectral
-----------------------

.. automodule:: neuropype_ephy.spectral
    :members:

