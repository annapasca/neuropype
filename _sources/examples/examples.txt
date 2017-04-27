.. _example:

Examples
========

All example scripts are based on the sample datasets provided by |OMEGA|.
In particular, we used the datasets organized according to the BIDS specifications (|BIDS|):
after the registration to the OMEGA website, the sample datatasets to use with the scripts can be downloaded from 
the |OMEGA_link|.

.. |OMEGA| raw:: html

   <a href="https://omega.bic.mni.mcgill.ca/main.php" target="_blank">OMEGA project</a>

.. |BIDS| raw:: html

   <a href="http://bids.neuroimaging.io" target="_blank">Brain Imaging Data Structure</a>

.. |OMEGA_link| raw:: html

   <a href="https://box.bic.mni.mcgill.ca/s/omega?path=%2FContributions%20(in%20BIDS%20format)" target="_blank">OMEGA link</a>

All example scripts need a :ref:`params` where to set 

* the list of subjects
* the data path 
* the parameters related to the preprocessing pipeline
* the parameters related to the connectivity pipeline
* the parameters related to the source reconstruction pipeline


 +---------------------------------------------+---------------------------------------------+
 | .. figure::  ../img/ICA_1comp.jpg           | .. figure::  ../img/graph_dot_conn2graph.jpg|
 |    :scale: 50 %                             |    :scale: 50 %                             |
 |    :align: center                           |    :align: center                           |
 |                                             |                                             |
 |    :ref:`preproc_example`                   |    :ref:`conn_graph_example`                |
 +---------------------------------------------+---------------------------------------------+
 | .. figure::  ../img/graph_epoch2graph.jpg   | .. figure::  ../img/graph_dot_inv2graph.jpg |
 |    :scale: 50 %                             |    :scale: 50 %                             |
 |    :align: center                           |    :align: center        	             |
 |                                             |                      		             |
 |    :ref:`epoch_example`                     |    :ref:`inv_example`                       |
 +---------------------------------------------+---------------------------------------------+  
 
 
.. toctree::
   :maxdepth: 1
   
   preproc_example
   conn_graph_example
   inv_example
   epoch_example
   
Scripts
+++++++

.. toctree::
   :maxdepth: 1

   params

   