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



