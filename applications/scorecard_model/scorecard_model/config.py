SELECTED_FEATURES = [
    'loan_amnt',
    'funded_amnt',
    'funded_amnt_inv',
    'fico_range_low',
    'fico_range_high',
    'total_pymnt',
    'total_pymnt_inv',
    'total_rec_prncp',
    'total_rec_int',
    'recoveries',
    'last_pymnt_amnt',
    'last_fico_range_high',
    'last_fico_range_low',
    'cr_line_age'
]

FEATURES = [
    'loan_amnt',
    'funded_amnt',
    'funded_amnt_inv',
    'fico_range_low',
    'fico_range_high',
    'total_pymnt',
    'total_pymnt_inv',
    'total_rec_prncp',
    'total_rec_int',
    'recoveries',
    'last_pymnt_amnt',
    'last_fico_range_high',
    'last_fico_range_low',
    'earliest_cr_line',
    'issue_d' 
]

NUMERICAL_VARIABLES = [
    'loan_amnt',
    'funded_amnt',
    'funded_amnt_inv',
    'fico_range_low',
    'fico_range_high',
    'total_pymnt',
    'total_pymnt_inv',
    'total_rec_prncp',
    'total_rec_int',
    'recoveries',
    'last_pymnt_amnt',
    'last_fico_range_high',
    'last_fico_range_low', 
    'cr_line_age'
]

DATE_VARIABLES = [
    'earliest_cr_line',
    'issue_d'
]
DUMP_FILE_PATH= 'scorecard_model/save_model_data'

SEED = 42

DATASET_PATH = 'scorecard_model/datasets/'
LENDING_CLUB_DATASET_URL = 'https://query.data.world/s/hpl2ah6z7juxta4qt6piqfiwpfn6i3'
TARGET = 'loan_status'

TARGET_MAP = {'Fully Paid' : 0,
              'Charged Off' : 1,
              'Does not meet the credit policy. Status:Fully Paid' : 0,
              'Does not meet the credit policy. Status:Charged Off' : 1,
              'Current' : 'Exclude',
              'In Grace Period' : 'Exclude',
              'Late (31-120 days)' : 'Exclude',
              'Late (16-30 days)' : 'Exclude',
              'Default' : 1}
