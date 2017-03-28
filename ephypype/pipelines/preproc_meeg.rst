.. _preproc_meeg:

Preprocessing pipeline
**********************

The preprocessing pipeline runs the ICA algorithm for an automatic removal of eyes and heart 
related artefacts. A report is automatically generated and can be used to correct and/or fine-tune the correction in each subject.

The pipeline is defined by the function :py:func:`create_pipeline_preproc_meeg <neuropype_ephy.pipelines.preproc_meeg.create_pipeline_preproc_meeg>`

Example and pictures:

...
