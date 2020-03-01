# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:44:23 2020

@author: Ege
"""
#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset= pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values # -1 means we take all the columns except last one.
Y = dataset.iloc[:,3].values

# Taking care of missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN', strategy = 'mean', axis= 0) #Missing datayı değiştmek için imputer objesi yarattık.
imputer =imputer.fit(X[:,1:3]) #Yarattığımız objeyi sadece missing data olan columnları kapsayacak şekilde X'e fit ettik.
X[:, 1:3] = imputer.transform(X[:, 1:3]) #Fonksiyonu uyguluyoruz, o değerleri değiştiriyoruz.

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
 
labelencoder_X = LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])  #Output: array([0, 2, 1, 2, 1, 0, 2, 0, 1, 0])
onehotencoder = OneHotEncoder(categorical_features=[0]) #categorical_features specifys which column are going to be treated as categorical data
X =onehotencoder.fit_transform(X).toarray()

labelencoder_Y = LabelEncoder()
Y=labelencoder_Y.fit_transform(Y)

# Splitting data to Training and Test Sets
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2, random_state = 0)

# Feature Scaling

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)
