""" Parameters file"""

import os

from params import *

data_type = 'fif'

# ------------------- SET source reconstruction variables ----------------#

# set sbj dir path, i.e. where the FS folfers are
sbj_dir = os.path.join(main_path, 'FSF')
noise_path = data_path

# set inverse parameters
spacing = 'oct-6'    # ico-5 vs oct-6
snr = 1.0            # use smaller SNR for raw data
inv_method = 'MNE'   # sLORETA, MNE, dSPM
parc = 'aparc'       # The parcellation to use: 'aparc' vs 'aparc.a2009s'

# noise covariance matrix filename template
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
                   'Right-Amygdala']
else:
    aseg_labels = []


# ----------------------- SET connectivity variables ----------------------#

freq_bands = [[8, 12], [13, 29]]
freq_band_names = ['alpha', 'beta']

# 'pli', 'plv', 'pli2_unbiased', 'coh', 'cohy', 'ppc', 'wpli'
# 'imcoh', 'wpli2_debiased', 'correl'
con_method = 'coh'
epoch_window_length = 3.0

# pipeline directory within the main_path dir
src_correl_analysis_name = 'spectral_connectivity_' + data_type + \
                            '_' + con_method + '_src_space_' + \
                            inv_method + '_' + parc.replace('.', '')
if aseg:
    src_correl_analysis_name = src_correl_analysis_name + '_aseg'


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

# mean_correl_permuts

nb_permuts = 5

mean_correl_permut_analysis_name = src_correl_analysis_name + "_permuts_" + \
    str(nb_permuts) + "_rada"  # ajouter "_rada" si decomposition de la matrice

mean_con_den = 0.05

if mod:
    # Radatools modularity optimisation sequence
    mean_radatools_optim = "WS trfr 1"
