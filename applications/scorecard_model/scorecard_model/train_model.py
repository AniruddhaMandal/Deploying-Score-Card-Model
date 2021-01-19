from scorecard_model import config
from scorecard_model import pipeline
from sklearn.model_selection import train_test_split
from scorecard_model.datasets import get_data
import joblib
from scorecard_model import preprocessors as pp
import pandas as pd

def train_model()->None:
    try:    
        data = pd.read_csv(config.DATASET_PATH+'LENDING_CLUB_DATASET.csv', low_memory=False)
    except:
        print('Data is missing.\n Downloading Dataset.....')
        data = get_data.download_dataset(config.LENDING_CLUB_DATASET_URL)
        print('Downloading Complete...')
    
    X = data[config.FEATURES]
    y = data[config.TARGET]
    X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=config.SEED)
    
    X_train, y_train = pp.drop_missing_target(X_train, y_train)
    y_train = pp.map_target_variable(y_train)
    X_train, y_train = pp.drop_exclude(X_train,y_train)
    

    log_reg_pipeline = pipeline.Logistic_regression_score_pipeline.fit(X_train, y_train)
    print('Pipeline Trained.')
    joblib.dump(log_reg_pipeline, config.DUMP_FILE_PATH+'/Logistic_regression_score_pipeline.pkl')
    print("Model Saved.")

if __name__ == '__main__':
    train_model()