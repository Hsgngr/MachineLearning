# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:10:08 2020

@author: Ege
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from sklearn.utils import resample

# Importing the dataset
# Read dataset
df= pd.read_csv('joined_data.csv', index_col='ID')
training=pd.read_csv(Path('brighton-a-memorable-city/training.csv'), index_col='ID')
X_test= pd.read_csv(Path('brighton-a-memorable-city/testing.csv'), index_col='ID')
#######################################################################################################################
from sklearn.experimental import enable_iterative_imputer  
from sklearn.impute import IterativeImputer

imputer = IterativeImputer(n_nearest_features=10,sample_posterior=True)
imputer.fit(training)
df=imputer.transform(df)
df=pd.DataFrame(data = df)
################################################################################################################

# Separate majority and minority classes
df_majority = df[df.iloc[:,4608]==1]
df_minority = df[df.iloc[:,4608]==0]
 
# Downsample majority class
df_majority_downsampled = resample(df_majority, 
                                 replace=False,    
                                 n_samples=1000)      

# reproducible results
df_minority_upsampled = resample(df_minority, 
                                 replace=True,     
                                 n_samples=1000)

# Combine minority class with downsampled majority class
df_downsampled = pd.concat([df_majority_downsampled, df_minority_upsampled])
 
# Display new class counts
df_downsampled.rename(columns={'4608': 'prediction'},inplace=True)
df_downsampled.rename(columns={4608: "prediction"},inplace=True)
df_downsampled.prediction.value_counts()

X=df_downsampled.iloc[:,:-1];
y=df_downsampled.iloc[:,-1];

#Add headers

#Extract columns that we are going to add
dataset=pd.read_csv('brighton-a-memorable-city/training.csv')
dataset= dataset.drop(['ID','prediction'],axis=1)
dataColumns= dataset.columns

#Add X column names
X.index=range(1,len(X)+1)
X.insert(0,'ID',value=X.index.astype('int64'))
X.set_index('ID', inplace=True)
X.columns=dataColumns

#Add Y column name
y.index = range(1,len(y)+1)
data=pd.concat([X,y],axis=1)
data.rename(columns={'4608': 'prediction'},inplace=True)
data.prediction=data.prediction.astype(int)
ID=data.index.values
data.insert(0,'ID',ID)
data.set_index('ID', inplace=True)
data.head()



data.to_csv('all_data_updown1000.csv')



