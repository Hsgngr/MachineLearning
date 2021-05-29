# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Import Libraries
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
#Split Train-Test Datasets
from sklearn.model_selection import train_test_split

train = pd.read_csv('titanic/train.csv')
test = pd.read_csv('titanic/test.csv')

print('train shape: ',train.shape)
print('test.shape',test.shape)

###############################################################################
#Check empty columns:
for column in train.columns:  
    print(column,' : ',any(train[column].isna()))
    
#Age, Cabin, Embarked has empty values

#HasCabin Feature:
train['hasCabin'] = (train['Cabin'].isna() ==False)
train['Cabin']  = train['Cabin'].replace(np.NaN,'empty')


def get_cabin_letter(string):
    
    print(string)
    if string != 'empty':    
        return string[0] 
    else:
        return 'X'

train['cabinLetter'] = train['Cabin'].apply(get_cabin_letter)

#CabinNumber

def get_cabin_number(string):
    if string != 'empty':
        cabin_list =  string.split()
        return len(cabin_list)
    else:
        return 0
    
train['CabinNumber'] = train['Cabin'].apply(get_cabin_number)


def get_train_type(string):
    if string.isdigit() == False:
        parts = string.split()
        return parts[0]
    else:
        return 'just_number'

ticket_types = train['Ticket'].apply(get_train_type)

from collections import Counter
print(Counter(ticket_types).most_common(4))
most_common_ticket_types = ['just_number','PC','C.A','STON/O']

ticket_categories = []
for ticket in ticket_types:
    
    if ticket not in most_common_ticket_types:
        ticket = 'other'
        
    ticket_categories.append(ticket)
    
train['Ticket_Category']  = ticket_categories

#Check categories
train['Ticket_Category'].value_counts()

np.clip(train['Fare'],0,150).hist(bins=10)

columns = ['Survived','Pclass','Sex','Age','SibSp','Parch','Fare','Embarked','cabinLetter','CabinNumber','Ticket_Category']
train_cleaned = train[columns]

y_train = train_cleaned.pop('Survived')

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

def categorize_df(train_cleaned):
    train_cleaned['Sex']= le.fit_transform(train_cleaned['Sex'])
    train_cleaned['Embarked'] = le.fit_transform(train_cleaned['Embarked'])
    train_cleaned['cabinLetter'] = le.fit_transform(train_cleaned['cabinLetter'])
    train_cleaned['CabinNumber'] = le.fit_transform(train_cleaned['CabinNumber'])
    train_cleaned['Ticket_Category'] = le.fit_transform(train_cleaned['Ticket_Category'])
    return train_cleaned

#Simpute
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_mean.fit(train_cleaned[['Age']])

train_cleaned['Age'] = imp_mean.transform(train_cleaned[['Age']])



from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(train_cleaned,y_train)
###############################################################################
test['hasCabin'] = (test['Cabin'].isna() ==False)
test['Cabin']  = test['Cabin'].replace(np.NaN,'empty')

test['cabinLetter'] = test['Cabin'].apply(get_cabin_letter)
test['CabinNumber'] = test['Cabin'].apply(get_cabin_number)

ticket_types = test['Ticket'].apply(get_train_type)
ticket_categories = []
for ticket in ticket_types:
    
    if ticket not in most_common_ticket_types:
        ticket = 'other'
        
    ticket_categories.append(ticket)
    
test['Ticket_Category']  = ticket_categories
columns = ['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked','cabinLetter','CabinNumber','Ticket_Category']

test_cleaned = test[columns]
test_cleaned = categorize_df(test_cleaned)
test_cleaned['Age'] = imp_mean.transform(test_cleaned[['Age']])

imp_mean.fit(train_cleaned[['Fare']])
test_cleaned['Fare'] = imp_mean.transform(test_cleaned[['Fare']])


y_pred = model.predict(test_cleaned)

y_pred = pd.DataFrame(y_pred)
y_pred['PassengerId'] = test['PassengerId']
y_pred=y_pred.rename(columns={0:'Survived'})
y_pred = y_pred[['PassengerId','Survived']]

y_pred.set_index('PassengerId',inplace=True,drop=True)
y_pred.to_csv('submission_1.csv')


sub = pd.read_csv('titanic/gender_submission.csv')
