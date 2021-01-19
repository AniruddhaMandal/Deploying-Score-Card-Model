import pandas as pd
from pandas.core.indexes.base import Index 
from scorecard_model import config 

def download_dataset(url):
    data = pd.read_csv(url, header = 1, low_memory=False)
    data.to_csv(f'{config.DATASET_PATH}LENDING_CLUB_DATASET.csv', index=False)
    return data 