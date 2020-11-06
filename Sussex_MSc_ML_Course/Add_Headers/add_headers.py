# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:51:43 2020

@author: Ege
"""

# Import Libraries
import pandas as pd
import numpy as np
from pathlib import Path


# Read dataset
all_data=pd.read_csv('downsampled_652.csv')
X = all_data.iloc[:,1:-1]
y =all_data.iloc[:,-1]

#Extract columns that we are going to add
df=pd.read_csv('brighton-a-memorable-city/training.csv')
df= df.drop(['ID','prediction'],axis=1)
dataColumns= df.columns

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

#Export the data
data.to_csv('IterativeImputed_downsampled652_headers.csv')
