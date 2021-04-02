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


"""
4) Try creating a single pipeline that does the full data preparation plus the final prediction
"""

"""
5) Automatically explore some preparation options using GridSearchCV
"""