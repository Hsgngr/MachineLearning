# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:33:57 2020

@author: Ege
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from sklearn.utils import resample

# Importing the dataset

df= pd.read_csv('joined_data.csv', index_col='ID')
confidence_annotations =pd.read_csv('brighton-a-memorable-city/annotation_confidence.csv', index_col='ID')

# Read dataset
X=df.iloc[:, df.columns != 'prediction']
y=df.prediction

X=pd.concat([X,confidence_annotations],axis=1)

dataset=pd.concat([X,y],axis=1)

dataset.to_csv('joined_data_with_confidence.csv')

    