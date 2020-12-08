# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:33:38 2020

@author: Ege

This script is based on Chapter 2: End-to-end Machine Learning Project in HandsOn ML Book starting from pg 46
"""

import os
import tarfile
import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url = HOUSING_URL, housing_path= HOUSING_PATH):
    os.makedirs(housing_path, exist_ok =True)
    tgz_path = os.path.join(housing_path,"housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path =housing_path)
    housing_tgz.close()
                
    
import pandas as pd

def load_housing_data(housing_path = HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

########################################################

fetch_housing_data(HOUSING_URL,HOUSING_PATH)
df = load_housing_data(HOUSING_PATH)

#Get the  info()
df.info()
df['ocean_proximity'].value_counts()
df.describe()

import matplotlib.pyplot as plt
df.hist(bins=50, figsize = (20,15))
plt.show()

#Split train-test sets
import numpy as np

def split_train_test(data,test_ratio):
    shuffled_indices =np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = split_train_test(df, 0.2)


from zlib import crc32

def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2 **32

def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_,test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

housing_with_id = df.reset_index() #adds an index column
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2 , "index")


from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(df,test_size = 0.2, random_state = 42)


#You learned median income is a very important attribute to predict median housing prices.
#You may want to ensure that the test set is representative of the various categories of incomes in the whole dataset
df['income_cat'] =  pd.cut(df['median_income'], bins = [0.,1.5,3.0,4.5,6.,np.inf], labels = [1,2,3,4,5])
df['income_cat'].hist()

#Now you are ready to satrified sampling based on the income category
from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits = 1, test_size = 0.2, random_state = 42)
for train_index, test_index in split.split(df, df['income_cat']):
    strat_train_set = df.loc[train_index]
    strat_test_set = df.loc[test_index]
    

# lets see if this worked as expected:
strat_test_set['income_cat'].value_counts() / len(strat_test_set)
df['income_cat'].value_counts() / len(df)

#Now you should remove the income_cat attribute so the data is back to its original state
for set_ in (strat_train_set, strat_test_set):
    set_.drop('income_cat', axis = 1, inplace= True)
    
#Let's make a copy of train_set for working on it without harming it:
housing = strat_train_set.copy()

#Visualizing Geographical Data
housing.plot(kind = 'scatter', x = 'longitude', y='latitude', alpha = 0.1)

housing.plot(kind = 'scatter', x = 'longitude', y= 'latitude', alpha = 0.4,
             s= housing['population']/100, label = 'population', figsize = (10,7),
             c = 'median_house_value', cmap =plt.get_cmap('jet'), colorbar= True,)
plt.legend()

#Looking for Correlations
corr_matrix = housing.corr()
corr_matrix['median_house_value'].sort_values(ascending = False)

from pandas.plotting import scatter_matrix

attributes = ['median_house_value', 'median_income','total_rooms', 'housing_median_age']
scatter_matrix(housing[attributes], figsize=(12,8))

'''
The main diagonal (top left to bottom right) would be full of straight lines if pandas
plotted each variable against itself, which would not be useful.
So instead pandas displays a histogram of each attribute
'''
#The most promising attribute to predict the median house value is the median income
housing.plot(kind = 'scatter', x= 'median_income', y = 'median_house_value', alpha = 0.1)

#Experimenting with Attribute Combinations
housing['rooms_per_household'] = housing['total_rooms'] /housing['households']
housing['bedrooms_per_room'] = housing['total_bedrooms'] / housing['total_rooms']
housing['population_per_household'] = housing['population'] / housing['households']

corr_matrix = housing.corr()
corr_matrix['median_house_value'].sort_values(ascending = False)

housing = strat_train_set.drop('median_house_value', axis = 1)
housing_labels = strat_train_set['median_house_value'].copy()

from _cleaning import DataCleaning

dataCleaning = DataCleaning()

dataCleaning.missingValues(housing)

dataset1 = dataCleaning.fixMissingValues(housing,subset =['total_bedrooms'],strategy = 'simpute')

#housing['ocean_proximity'] has categorical data lets convert that from text to numbers
from sklearn.preprocessing import OrdinalEncoder
ordinal_encoder = OrdinalEncoder()
housing_cat_encoded = ordinal_encoder.fit_transform(dataset1)

from sklearn.preprocessing import OneHotEncoder
cat_encoder = OneHotEncoder()
housing_cat_1hot = cat_encoder.fit_transform(dataset1)

#This create a SciPy array. In order to use as a dense Numpy array use:
housing_2 = housing_cat_1hot.toarray()


#Custom Transformers
from sklearn.base import BaseEstimator, TransformerMixin

rooms_ix, bedrooms_ix, population_ix, households_ix = 3,4,5,6

class CombinedAttributesAdder(BaseEstimator,TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): #no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
        
    def fit(self,X,y=None):
        return self #nothing else to do
    
    def transform(self,X):
        rooms_per_household = X[:,rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:,rooms_ix] / X[:,households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room= X[:, bedrooms_ix] / X[:,rooms_ix]
            return np.c_[X,rooms_per_household,population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]
    
attr_adder = CombinedAttributesAdder(add_bedrooms_per_room = True)
housing_extra_attribs = attr_adder.transform(housing.values)

#Transformation Pipelines
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy = "median")),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler()),
    ])

housing_num = housing.drop('ocean_proximity', axis = 1)
housing_num_tr = num_pipeline.fit_transform(housing_num)

from sklearn.compose import ColumnTransformer

num_attribs = list(housing_num)
cat_attribs = ['ocean_proximity']

full_pipeline =  ColumnTransformer([
    ('num',num_pipeline, num_attribs),
    ('cat', OneHotEncoder(), cat_attribs)])

housing_prepared = full_pipeline.fit_transform(housing)


import joblib

joblib.dump(housing_prepared,'housing_prepared.pkl')
joblib.dump(housing_labels,'housing_labels.pkl')