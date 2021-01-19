from scorecard_model import config 
from sklearn.pipeline import Pipeline
import scorecard_model.preprocessors as pp
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

Logistic_regression_score_pipeline = Pipeline([
    
    
    ('convert_datetime', pp.Date_variable_constructor(variables=config.DATE_VARIABLES, drop_file_path=config.DUMP_FILE_PATH),),


    ('day_difference', pp.Day_difference(variables=config.DATE_VARIABLES, drop_file_path=config.DUMP_FILE_PATH, name='cr_line_age'),),


    ('numerical_imputer', pp.Numerical_missing_values(variables=config.NUMERICAL_VARIABLES, drop_file_path=config.DUMP_FILE_PATH),),


    ('standard_scaler', StandardScaler(),),


    ('logistic_regression', LogisticRegression(random_state=config.SEED),),
])