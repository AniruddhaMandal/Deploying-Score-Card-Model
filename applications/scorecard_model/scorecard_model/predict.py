import joblib 
from scorecard_model import config
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import roc_auc_score
import pandas as pd
from scorecard_model import preprocessors as pp

data = pd.read_csv(f'{config.DATASET_PATH}LENDING_CLUB_DATASET.csv', low_memory=False)
X = data[config.FEATURES]
y = data[config.TARGET]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=config.SEED)
X_test,y_test = pp.drop_missing_target(X_test, y_test)
y_test = pp.map_target_variable(y_test)
X_test,y_test = pp.drop_exclude(X_test, y_test)
log_reg_model = joblib.load(config.DUMP_FILE_PATH+'/Logistic_regression_score_pipeline.pkl')
y_predict = log_reg_model.predict_proba(X_test)

roc_auc_score = roc_auc_score(y_test ,y_predict[:, 1])

print("ROC_AUC_SCORE:",roc_auc_score)