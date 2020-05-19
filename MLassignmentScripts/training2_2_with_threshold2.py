# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:40:09 2020

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
X_train, X_cv, y_train, y_cv = train_test_split(X, y, test_size = 0.25)

#Fitting RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
features = list(X_train.columns)
classifier = RandomForestClassifier(n_estimators=10000, n_jobs=-1, class_weight={0:0.17, 1:0.83})
classifier.fit(X_train,y_train)

y_cv_pred= classifier.predict(X_cv)
y_cv_pred=pd.DataFrame(data =y_cv_pred)
classifier.score(X_cv,y_cv)     
                                                   #Bunu yaptığımızda y_cv_prediction'ı koymamıza gerek yok o zaman içinde internally predictionu yapıyor.

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
y_cv_pred_pred=classifier.predict(X_cv)
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
y_pred = classifier.predict_proba(X_test)
threshold=0.4
y_pred [:,0] = (y_pred [:,0] < threshold).astype('int')
y_pred=pd.DataFrame(data=y_pred)
y_pred = y_pred.astype('int')
y_pred.drop(columns=[1], inplace=True)

#Exporting the results as csv file:
y_pred=pd.DataFrame(data=y_pred)
ID=X_test.index.values
y_pred.insert(0,'ID',ID)
y_pred=y_pred.rename(columns={0: 'prediction'})
y_pred.set_index('ID', inplace=True)
y_pred.to_csv('y_pred_upsampled_RandomForest2_with_threshold.csv')
y_pred.prediction.value_counts(normalize= True)
