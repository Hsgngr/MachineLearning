# -*- coding: utf-8 -*-
"""
Created on Mon May 25 21:37:52 2020

@author: Ege
"""
sample_rate=0.1
num_of_samples=int(len(X_test)*sample_rate)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_cv, y_train, y_cv = train_test_split(train_removed, y, test_size = 0.25)

model.fit(X_train,y_train)   
pseudo_labels=model.predict_proba(X_test)

threshold=0.5
pseudo_labels [:,0] = (pseudo_labels [:,0] < threshold).astype('int')
pseudo_labels=pd.DataFrame(data=pseudo_labels)
pseudo_labels = pseudo_labels.astype('int')
pseudo_labels.drop(columns=[1], inplace=True)

X_test=pd.DataFrame(data=X_test)
ID=X_test.index.values
pseudo_labels.insert(0,'ID',ID)
pseudo_labels=pseudo_labels.rename(columns={0: 'prediction'})
pseudo_labels.set_index('ID', inplace=True)
pseudo_labels.prediction.value_counts(normalize= True)



# Add the pseudo-labels to the test set
pseudo_data = X_test.copy(deep=True)
pseudo_data.insert(1674,'prediction',pseudo_labels)

# Take a subset of the test set with pseudo-labels and append in onto the training set
from random import sample 
sampled_pseudo_data = pseudo_data.sample(n=num_of_samples)
temp_train = pd.concat([train_removed, y], axis=1)
augemented_train = pd.concat([sampled_pseudo_data, temp_train])
augemented_train=shuffle(augemented_train)
 

#Fit the model with new data
model.fit(augemented_train.iloc[:,:-1],augemented_train['prediction'])

# Predicting the Test set results
y_pred =model.predict_proba(X_test)
threshold=0.5
y_pred [:,0] = (y_pred [:,0] < threshold).astype('int')
y_pred=pd.DataFrame(data=y_pred)
y_pred = y_pred.astype('int')
y_pred.drop(columns=[1], inplace=True)

X_test=pd.DataFrame(data=X_test)
ID=X_test.index.values
y_pred.insert(0,'ID',ID)
y_pred=y_pred.rename(columns={0: 'prediction'})
y_pred.set_index('ID', inplace=True)
y_pred.prediction.value_counts(normalize= True)

#Exporting the results as csv file:

y_pred.to_csv('Inbox/y_pred_updown1000_1674features_semi_supervised.csv')

