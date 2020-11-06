# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:56:43 2020

@author: Ege
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Importing the dataset
dataset=pd.read_csv(Path('Imbalanced_data/data_upsammpled.csv'), index_col=0)
X=dataset.iloc[:, dataset.columns != 'prediction']
y=dataset.prediction
X_test= pd.read_csv(Path('brighton-a-memorable-city/testing.csv'), index_col='ID')

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_cv, y_train, y_cv = train_test_split(X, y, test_size = 0.25, random_state = 0)

########################################################################################################
#Fitting Ann

# Importing the Keras libraries and packages
import tensorflow as tf


# Initializing the ANN
ann = tf.keras.models.Sequential()

# Adding the input layer and the first hidden layer
ann.add(tf.keras.layers.Dense(32, input_dim=4608))

# Adding the second hidden layer
ann.add(tf.keras.layers.Dense(units=32, activation='relu'))
ann.add(tf.keras.layers.Dense(units=32, activation='relu'))
ann.add(tf.keras.layers.Dense(units=32, activation='relu'))



# Adding the output layer
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Part 3 - Training the ANN

# Compiling the ANN
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Training the ANN on the Training set
ann.fit(X_train, y_train, batch_size = 64, epochs = 100)
  
y_cv_pred= ann.predict(X_cv)
y_cv_pred=pd.DataFrame(data =y_cv_pred)  
y_cv_pred = (y_cv_pred > 0.5)
                     
#########################################################################################################################
#Detailed Report
from sklearn.metrics import classification_report
print(classification_report(y_cv, y_cv_pred))


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_cv, y_cv_pred)
print(cm)

#Roc Analization
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
y_cv_pred_pred=ann.predict(X_cv)
fpr,tpr,threshold=roc_curve(y_cv,y_cv_pred)
auc = roc_auc_score(y_cv, y_cv_pred)
print('AUC: %.3f' % auc)
plt.plot(fpr, tpr)
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.show()

#Importing the test dataset
X_test= pd.read_csv(Path('brighton-a-memorable-city/testing.csv'), index_col=0)

# Predicting the Test set results
y_pred = ann.predict(X_test)
y_pred =(y_pred > 0.5).astype(int)
#Exporting the results as csv file:
y_pred=pd.DataFrame(data=y_pred)
ID=X_test.index.values
y_pred.insert(0,'ID',ID)
y_pred=y_pred.rename(columns={0: 'prediction'})
y_pred.set_index('ID', inplace=True)
y_pred.to_csv('y_pred_upsampled_ann_epoch1000_layer12_unit128.csv')
