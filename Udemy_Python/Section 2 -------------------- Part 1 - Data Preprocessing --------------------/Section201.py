# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:44:23 2020

@author: Ege
"""
#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset= pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values # -1 means we take all the columns except last one.
Y = dataset.iloc[:,3].values

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN', strategy = 'mean', axis= 0)
imputer =imputer.fit(X[:,1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])