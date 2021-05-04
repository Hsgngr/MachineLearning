# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:39:19 2021

@author: Ege
"""
"""
1) Try a Support Vector Machine regressor (sklearn.svm.SVR) with various hyperparameters,
such as kernel = "linear" (with various values for the C hyperparameter) or kernel="rbf"
(with various values for the C and gamma hyperparameters).

How does the best SVR predictor perform ?
"""
import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor

housing_prepared= joblib.load('housing_prepared.pkl')
housing_labels = joblib.load('housing_labels.pkl')
#GridSearch
param_grid = [
    {'kernel': ['linear'], 'C': [1,1.2,1.5,2,4]},
    {'kernel': ['rbf','poly','sigmoid'],'C': [1,1.2,1.5,2,4],'gamma': ['scale','auto']}
    ]


svr_reg = SVR()

grid_search = GridSearchCV(svr_reg, param_grid, cv = 5, scoring = 'neg_mean_squared_error',
                          return_train_score = True)
grid_search.fit(housing_prepared,housing_labels)
print(grid_search.best_params_)

#Get feature importances (for exercise 3):
feature_importances = grid_search.best_estimator_.feature_importances_

"""
2) Try replacing GridSearchCV with RandomizedSearchCV
"""
from sklearn.model_selection import RandomizedSearchCV

param_grid = [
    {'kernel': ['linear'], 'C': [4,5,6,7,8]}]
randomized_search = RandomizedSearchCV(svr_reg,param_grid,cv=5, scoring= 'neg_mean_squared_error',
                                       return_train_score=True)

randomized_search.fit(housing_prepared,housing_labels)
print(randomized_search.best_params_)

"""
3) Try adding a transformer in the preparation pipeline to select only important attributes
"""
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

rfr =  RandomForestRegressor()
rfr.fit(housing_prepared,housing_labels)

feature_importances = rfr.feature_importances_

def indices_of_top_k(arr,k):
    return np.sort(np.argpartition(np.array(arr), -k)[-k:])

class TopFeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, feature_importances, k):
        self.feature_importances =  feature_importances
        self.k = k
        
    def fit(self,X,y= None):
        self.feature_indices_ = indices_of_top_k(self.feature_importances,self.k)
        return self
    def transform(self, X):
        return X[:,self.feature_indices_]
    
    
#Lets define the number of features that we would like to keep:
k = 5

#Lets look for the indices of the top k features:
top_k_feature_indices = indices_of_top_k(feature_importances, k)

import pandas as pd
df =  pd.read_csv('D:/Works/MachineLearning/Handson_ML/Chapter II (End-to-end ML Project)/datasets/housing/housing.csv')

attributes = "the datasets columns"
np.array(attributes)[top_k_feature_indices]

"""
array(['longitude', 'latitude', 'median_income', 'pop_per_hhold',
       'INLAND'], dtype='<U18')

"""
preparation_and_feature_selection_pipeline = Pipeline([
    ('preparation', full_pipeline),
    ('feature_selection', TopFeatureSelector(feature_importances, k))
])

housing_prepared_top_k_features = preparation_and_feature_selection_pipeline.fit_transform(housing)

"""
4) Try creating a single pipeline that does the full data preparation plus the final prediction
"""
from sklearn.pipeline import Pipeline

single_pipeline_rules_them_all = Pipeline([
    ('preparation', full_pipeline),
    ('feature_selection', TopFeatureSelector(feature_importances,k)),
    ('model', rfr)])
"""
5) Automatically explore some preparation options using GridSearchCV
"""
param_grid = [{
    'preparation__num__imputer__strategy': ['mean', 'median', 'most_frequent'],
    'feature_selection__k': list(range(1, len(feature_importances) + 1))
}]

grid_search_prep = GridSearchCV(prepare_select_and_predict_pipeline, param_grid, cv=5,
                                scoring='neg_mean_squared_error', verbose=2)
grid_search_prep.fit(housing, housing_labels)