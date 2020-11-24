
"""

@author: Ege
"""
# numpy and pandas for data manipulation
import numpy as np
import pandas as pd

# visualizations
import matplotlib.pyplot as plt
import seaborn as sns

#Formatting
from decimal import *

#Sklearn
from sklearn.impute import SimpleImputer

# __all__ affects how from _cleaning import  * works. It only imports the objects in the array
__all__ = []


class DataCleaning():
    
    '''
    Class for performing data cleaning for machine learning or data science
    Implements 2 different process for data cleaning
    
        1. Handling Missing Values
        2. Handling Text, Categorical Data
        3. Feature Scaling
        4. Feature Selection
        
        
    '''    
    def __init__(self, dataset= None):
        self.dataset = dataset
        
        
    def missingValues(self,data, printResults = True):
        ''''Checks if there is any missingValues and show them in a nice format'''
        
        columns = [] #Columns with missing values
        
        if data.isnull().sum().sum() < 1:
            print('\nThere is no missing data as Nan. If you still not sure check the Dataframe manually')
        
        else:
            if printResults == True:
                print('\nColumns with Missing Values:')
                
            for column in data.columns:
                missing_count= data[column].isnull().sum()
                if missing_count >1:
                    missing_ratio = missing_count / len(column)
                    missing_ratio = float("{:.2f}".format(missing_ratio))
                    columns.append(column)
                    #If the missing rate higher than 5% show the percentage
                    if printResults == True:
                        if missing_ratio >5:      
                            print('{} : {} ({} % is missing)' .format(column,missing_count,missing_ratio))
                        else:
                            print('{} : {}'.format(column,missing_count))
            if printResults == True:                
                print('\nThere are totally {} missing values in the dataset'.format(data.isnull().sum().sum()))
            
            return columns
            
    def fixMissingValues(self,data, subset = None, strategy ='simpute', simpute_option= 'mean', fill_value = None):
                         
        '''
        There are 3 options for fixing the Missing Values
        1. Get rid of the corresponding district
        2. Get rid of the whole attribute
        3. Set the values to some value (Imputing)
        
        Parameters 
        --------
        
        data : DataFrame
            The dataframe that you are going to use
            
        subset : stringList, default = None
            column name or list of column names. If you only want to fix given columns

        strategy : string, default= 'simpute'
            
            * drop_examples
            * drop_columns
            * simpute
            
        simpute_option: default = 'mean'
            If you use simpute strategy default mean is used.
            
            * 'mean': replace missing values using the mean along each column.
            
            * 'median': replace missing values using median along each column.
            
            * 'most_frequent': replace  missing values using most frequent value along each column.
            
            * 'constant'
                If you use constant then replace missing values with fill_value
        
        fill_value: string or numerical value, default = None
            
            * Use this parameter if you use constant option of Simple Imputer
            
            
        Return
        --------
        data: dataframe
            Dataframe with filled or removed missing values.
        '''
        
        columns = self.missingValues(data, printResults=False)
        if columns is None:
            return data
        
        if subset is not None:
            columns = subset
            
        if strategy == 'drop_examples':
           data = data.dropna(subset= columns)
        
        if strategy == 'drop_columns':
           data = data.drop(columns,axis = 1)
        
        if strategy == 'simpute':
            imputer = SimpleImputer(strategy = simpute_option, fill_value=fill_value)
            imputer.fit(data[columns])
            X = imputer.transform(data[columns])
            data[columns] = X
        
        return data
            
            