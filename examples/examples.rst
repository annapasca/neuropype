.. _example:

Examples
========

All example scripts are based on the sample datasets provided by |OMEGA|.
In particular, we used the datasets organized according to the BIDS specifications (|BIDS|):
after the registration to the |OMEGA_registration|, the sample datatasets to use with the scripts can be downloaded from 
the |OMEGA_link|.

.. |OMEGA| raw:: html

   <a href="https://omega.bic.mni.mcgill.ca/main.php" target="_blank">OMEGA project</a>

.. |BIDS| raw:: html

   <a href="http://bids.neuroimaging.io" target="_blank">Brain Imaging Data Structure</a>

.. |OMEGA_link| raw:: html

   <a href="https://box.bic.mni.mcgill.ca/s/omega?path=%2FContributions%20(in%20BIDS%20format)" target="_blank">OMEGA link</a>
   
.. |OMEGA_registration| raw:: html

   <a href="https://www.mcgill.ca/bic/omega-registration" target="_blank">OMEGA website</a>



All example scripts need a :ref:`params` where to set 

* the list of subjects
* the data path 
* the parameters related to the preprocessing pipeline
* the parameters related to the connectivity pipeline
* the parameters related to the source reconstruction pipeline


 +---------------------------------------------+---------------------------------------------+
 | .. figure::  ../img/ICA_1comp.jpg           | .. figure::  ../img/power.jpg               |
 |    :scale: 40 %                             |    :scale: 40 %                             |
 |    :align: center                           |    :align: center                           |
 |                                             |                                             |
 |    :ref:`preproc_example`                   |    :ref:`power_example`                     |
 +---------------------------------------------+---------------------------------------------+
 | .. figure::  ../img/graph_coclass.jpg       | .. figure::  ../img/circle_conmat_coh.jpg   |
 |    :scale: 40 %                             |    :scale: 40 %                             |
 |    :align: center                           |    :align: center        	             |
 |                                             |                      		             |
 |    :ref:`conn_graph_example`                |    :ref:`inv_example`                       |
 +---------------------------------------------+---------------------------------------------+  
 
 
.. toctree::
   :maxdepth: 1
   
   preproc_example
   power_example
   conn_graph_example
   inv_example
   
.. toctree::
   :maxdepth: 3

   howto
   
   
Scripts
-------

.. toctree::
   :maxdepth: 1

   params

   