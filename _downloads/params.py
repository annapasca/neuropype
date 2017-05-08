""" Parameters file"""

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

    is_set_ICA_components = False

    if is_set_ICA_components:
        n_comp_exclude = {'sub-0002': {'ses-0001': [0, 1, 3]}}
    else:
        n_comp_exclude = []


# -------------------------- SET power variables --------------------------#
data_type = 'fif'
data_folder = 'Cleaned&epoched_files'
power_analysis_name = 'power_pipeline'
fmin = 0
fmax = 300
power_method = 'welch'
is_epoched = False


# ----------------------- SET connectivity variables ----------------------#

freq_bands = [[2, 4], [5, 7], [8, 12], [13, 29], [30, 59], [60, 90]]
freq_band_names = ['delta', 'theta', 'alpha', 'beta', 'gamma1', 'gamma2']

# 'pli', 'plv', 'pli2_unbiased', 'coh', 'cohy', 'ppc', 'wpli'
# 'imcoh', 'wpli2_debiased', 'correl'
con_method = 'coh'
epoch_window_length = 3.0

# pipeline directory within the main_path dir
correl_analysis_name = 'spectral_connectivity_' + data_type + \
                            '_' + con_method


# ------------------- SET source reconstruction variables ----------------#

# set sbj dir path, i.e. where the FS folfers are
sbj_dir = os.path.join(main_path, 'derivatives/freesurfer/')
noise_path = data_path

# set inverse parameters
spacing = 'oct-6'    # ico-5 vs oct-6
snr = 1.0            # use smaller SNR for raw data
inv_method = 'MNE'   # sLORETA, MNE, dSPM
parc = 'aparc'    # The parcellation to use: 'aparc' vs 'aparc.a2009s'

# noise covariance matrix computed by room empty data
noise_cov_fname = '*noise*.ds'

'''
aseg_labels = ['Left-Accumbens-area',
               'Left-Amygdala',
               'Left-Caudate',
               'Left-Hippocampus',
               'Left-Pallidum',
               'Left-Putamen',
               'Left-Thalamus-Proper',
               'Left-Cerebellum-Cortex',
               'Brain-Stem',
               'Right-Accumbens-area',
               'Right-Amygdala',
               'Right-Caudate',
               'Right-Hippocampus',
               'Right-Pallidum',
               'Right-Putamen',
               'Right-Thalamus-Proper',
               'Right-Cerebellum-Cortex']
'''
aseg = False
if aseg:
    aseg_labels = ['Left-Amygdala',
                   'Left-Hippocampus',
                   'Left-Thalamus-Proper',
                   'Left-Cerebellum-Cortex',
                   'Brain-Stem',
                   'Right-Amygdala',
                   'Right-Hippocampus',
                   'Right-Thalamus-Proper',
                   'Right-Cerebellum-Cortex']
    aseg_labels = ['Left-Amygdala',
                   'Right-Amygdala']
else:
    aseg_labels = []


# ---------------------------- SET graph variables -----------------------#
freq_con_thr = [0.05] * 7  # TODO is it used???
con_den = 0.05

if con_method == "correl":
    conf_interval_prob = 0.05

Z_thr = 1.6

# compute modularity (True or False)
mod = True

if mod:
    # Radatools modularity optimisation sequence
    radatools_optim = "WS trfr 1"

# coclass
coclass_thr = 30

coclass_analysis_name = "coclass_" + data_type + "_" + \
                         str(coclass_thr) + "_rada" 

if test:
    coclass_analysis_name = coclass_analysis_name + '_test'
    
# mean_correl_permuts

nb_permuts = 5

mean_correl_permut_analysis_name = correl_analysis_name + "_permuts_" + str(nb_permuts) + "_rada" ### ajouter "_rada" si decomposition de la matrice

mean_con_den = 0.05

if mod:
# Radatools modularity optimisation sequence
    mean_radatools_optim = "WS trfr 1"
