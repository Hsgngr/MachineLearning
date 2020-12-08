# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:56:04 2020

@author: Ege
"""
#Part 2 of understanding_data
import pandas as pd
import numpy as np


import joblib

housing_prepared= joblib.load('housing_prepared.pkl')
housing_labels = joblib.load('housing_labels.pkl')


from sklearn.linear_model import LinearRegression


lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)


#It works eventhough the predictions are not that much accurate.

from sklearn.metrics import mean_squared_error
housing_predictions = lin_reg.predict(housing_prepared)
lin_mse = mean_squared_error(housing_labels, housing_predictions)
lin_rmse = np.sqrt(lin_mse)
lin_rmse


from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor()
tree_reg.fit(housing_prepared, housing_labels)

housing_predictions = tree_reg.predict(housing_prepared)
tree_mse = mean_squared_error(housing_labels, housing_predictions)
tree_rmse = np.sqrt(tree_mse)
tree_rmse

'''
One way to evaluate the Decision Tree model would be to use 
the train_test_split() function to split the training set into a smaller training set 
and a validation set, then train your models against smaller training set and evaluate
them against the validation set.
'''
from sklearn.model_selection import cross_val_score
scores =cross_val_score(tree_reg, housing_prepared,housing_labels, scoring = "neg_mean_squared_error",cv= 10)
tree_rmse_scores =  np.sqrt(-scores)


def display_scores(scores):
    print('Scores: ',scores)
    print('Mean: ', scores.mean())
    print('Standard Deviation: ', scores.std())
    
display_scores(tree_rmse_scores)


#Lastly lets try RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor
forest_reg = RandomForestRegressor()
forest_reg.fit(housing_prepared, housing_labels)

housing_predictions = forest_reg.predict(housing_prepared)
forest_mse = mean_squared_error(housing_labels, housing_predictions)
forest_rmse = np.sqrt(forest_mse)
forest_rmse

scores =cross_val_score(forest_reg, housing_prepared,housing_labels, scoring = "neg_mean_squared_error",cv= 10)
forest_rmse_scores =  np.sqrt(-scores)

display_scores(forest_rmse_scores)


import joblib

joblib.dump(housing_prepared,'housing_prepared.pkl')
joblib.dump(housing_labels,'housing_labels.pkl')


housing_prepared= joblib.load('housing_prepared.pkl')
housing_labels = joblib.load('housing_labels.pkl')


#GridSearch
from sklearn.model_selection import GridSearchCV

param_grid = [
    {'n_estimators': [3,10,30], 'max_features': [2,4,6,8]},
    {'bootstrap': [False], 'n_estimators': [3,10], 'max_features': [2,3,4]}]

forest_reg = RandomForestRegressor()

grid_search = GridSearchCV(forest_reg, param_grid, cv = 5, scoring = 'neg_mean_squared_error',
                          return_train_score = True)

grid_search.fit(housing_prepared,housing_labels)
grid_search.best_params_

feature_importances = grid_search.best_estimator_.feature_importances_