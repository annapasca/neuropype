""" Parameters file for run_preprocess_pipeline.py """

import os

test = True

data_type = 'ds'

main_path = '/run/media/pasca/paska/meg_data/omega/sample_BIDS_omega/'
if test:
    data_type = 'fif'

data_path = main_path

subject_ids = ['sub-0002', 'sub-0003', 'sub-0004', 'sub-0006', 'sub-0007']
sessions = ['ses-0001']

down_sfreq = 800
l_freq = 0.1
h_freq = 150


# ------------------------ SET ICA variables -----------------------------#

is_ICA = True  # if True we apply ICA to remove ECG and EoG artifacts

# specify ECG and EoG channel names if we know them
ECG_ch_name = 'ECG'
EoG_ch_name = 'HEOG, VEOG'
variance = 0.95

reject = dict(mag=5e-12, grad=5000e-13)

# pipeline directory within the main_path dir
preproc_pipeline_name = "preprocessing_pipeline"
if test:
    preproc_pipeline_name = preproc_pipeline_name + '_test'

    is_set_ICA_components = True

    if is_set_ICA_components:
        n_comp_exclude = {'sub-0002': {'ses-0001': [0, 1, 3]}}
    else:
        n_comp_exclude = []


