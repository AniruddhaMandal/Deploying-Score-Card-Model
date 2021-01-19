import numpy as np 
import pandas as pd 
from sklearn.base import BaseEstimator, TransformerMixin
from scorecard_model import config

class Numerical_missing_values(BaseEstimator, TransformerMixin):
    def __init__(self, variables = None, drop_file_path='./'):
        if not isinstance(variables,list):
            self.variables = [variables]
        else:
            self.variables = variables
        self.drop_file_path = drop_file_path 

    def fit(self, X:pd.DataFrame, y:pd.Series=None )->"Numerical_missing_values":
        self.missing_num_values_dict = {}
        for feature in self.variables:
            self.missing_num_values_dict[feature] = X[feature].mode()[0]
        np.save(f'{self.drop_file_path}/missing_num_variables_dict.npy',self.missing_num_values_dict)
        return self 

    def transform(self, X:pd.DataFrame)->pd.DataFrame:
        X = X.copy()
        for feature in self.variables:
            X[feature].fillna(self.missing_num_values_dict[feature], inplace=True)
        return X

class Date_variable_constructor(BaseEstimator, TransformerMixin):
    def __init__(self, variables = None, drop_file_path='./'):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
        self.drop_file_path = drop_file_path
    
    def fit(self, X: pd.DataFrame, y: pd.Series)->"Date_variable_constructor":
        self.datetime_dict = {}
        for var in self.variables:
            self.datetime_dict[var] = pd.to_datetime(X[var])
        np.save(f'{self.drop_file_path}/datetime_dict.npy', self.datetime_dict)
        return self

    def transform(self, X: pd.DataFrame)-> pd.DataFrame:
        X = X.copy()
        for var in self.variables:
            X[var] = self.datetime_dict[var]
            
        return X

class Day_difference(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None,name='Day_difference', drop_file_path='./'):
        if len(variables)==2:    
            self.variables = variables
        else:
            self.variables = ["issue_d", 'earliest_cr_line'] 
        self.drop_file_path = drop_file_path
        self.name = name

    def fit(self, X:pd.DataFrame, y: pd.Series)->"Day_difference":
        day_difference = X[self.variables[1]]-X[self.variables[0]]
        self.day_difference = day_difference/np.timedelta64(1,'D')
        return self
    
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        X[self.name] = self.day_difference
        droped_variables = {
            0: self.variables[0],
            1: self.variables[1]
        }
        np.save(f'{self.drop_file_path}/droped_datetime_variables.npy', droped_variables)
        X.drop(self.variables, axis=1, inplace=True)
        return X

def drop_missing_target(X, y):
    drop_index = y[y.isnull() == True].index
    np.save(f"{config.DUMP_FILE_PATH}/missing_target_index.npy", drop_index)
    X = X.copy()
    y = y.copy()
    X.drop(drop_index, inplace=True)
    y.drop(drop_index, inplace=True)
    return X, y

def map_target_variable(y):
    y = y.copy()
    y = y.map(config.TARGET_MAP)
    return y

def drop_exclude(X,y):
    X = X.copy()
    y = y.copy()
    drop_index = y.loc[y=='Exclude'].index
    X.drop(drop_index, inplace=True)
    y.drop(drop_index, inplace=True)
    y = y.astype('int64')
    return X,y