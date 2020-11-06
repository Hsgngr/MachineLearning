# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:34:05 2020

@author: Ege
"""


import pandas as pd
import numpy as np

#Import the data
data=pd.read_csv('Simputed_with_mean_with_X_test_headers.csv',index_col= 0)

    
#Split to dataset to majority/minority
data_majority = data[data.prediction==1]
data_minority = data[data.prediction==0]

#Upsample the minority

from sklearn.utils import resample
# Upsample minority class
data_minority_upsampled = resample(data_minority, 
                                 replace=True,     # sample with replacement
                                 n_samples=2140,    # to match majority class
                                 random_state=123) # reproducible results

# Combine majority class with upsampled minority class
data_upsampled = pd.concat([data_majority, data_minority_upsampled])
 
# Display new class counts
data_upsampled.prediction.value_counts()

#Export the data:
    
data_upsampled.to_csv('Simputed_with_mean_with_X_test_upsampled.csv')

