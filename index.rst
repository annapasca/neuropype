.. neuropype_ephy documentation master file, created by
   sphinx-quickstart on Wed Feb 22 13:05:03 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


NeuroDaddy documentation
************************

NeuroDaddy is an open-source multi-modal brain data analysis kit which provides **Python-based 
pipelines** for advanced multi-thread processing of fMRI, MEG and EEG data, with a focus on connectivity 
and graph analyses. NeuroDaddy is based on `Nipype <http://nipype.readthedocs.io/en/latest/#>`_,
a tool developed in fMRI field, which facilitates data analyses by wrapping many commonly-used neuro-imaging software into a common
python framework.

NeuroDaddy project includes two different packages:

* :ref:`ephypype` based on `MNE python <http://martinos.org/mne/stable/index.html>`_ includes pipelines for electrophysiology analysis
* `graphpype <http://davidmeunier79.github.io/neuropype_graph/>`_ based on `radatools <http://deim.urv.cat/~sergio.gomez/radatools.php>`_ includes pipelines for graph theoretical analysis of neuroimaging data 

NeuroDaddy provides a very common and fast framework to develop workflows for advanced analyses, in particular
defines a set of different pipelines that can be used stand-alone or as lego of a bigger workflow:
the input of a pipeline will be the output of another pipeline. 

For each possible workflow the input data can be specified in three different ways: 

* raw MEG data in .fif and .ds format 
* time series of connectivity matrices in .mat (Matlab) or .npy (Numpy) format
* connectivity matrices in .mat (Matlab) or .npy (Numpy) format

.. _lego:

.. figure::  img/all_input_doors.png
   :align:   center

   Main inputs and subsequent pipeline steps

Each pipeline based on nipype engine is defined by nodes connected together, 
where each node maybe wrapping of existing software (as MNE-python modules or radatools functions) 
as well as providing easy ways to implement function defined by the user. 

:ref:`example`

Installation
============

::

      git clone ...

Packages
========

.. toctree::
   :maxdepth: 1

   ephypype/neuropype_ephy
   graphpype <http://davidmeunier79.github.io/neuropype_graph/>
   examples/examples 
   graphpype/index

   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

