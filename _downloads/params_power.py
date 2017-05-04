""" Parameters file for run_power_analysis.py """

test = True

data_type = 'fif'

main_path = '/run/media/pasca/paska/meg_data/omega/sample_BIDS_omega/'
data_path = main_path

subject_ids = ['sub-0002', 'sub-0003', 'sub-0004', 'sub-0006', 'sub-0007']
sessions = ['ses-0001']

# -------------------------- SET power variables --------------------------#
fmin = 0
fmax = 300
power_method = 'welch'
is_epoched = False

power_analysis_name = 'power_pipeline'

