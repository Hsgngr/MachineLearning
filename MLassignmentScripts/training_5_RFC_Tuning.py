# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:21:48 2020

@author: Ege
"""



# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

data=pd.read_csv(Path('all_data_updown1000.csv'), index_col=0)
X=data.iloc[:,:4096]
y=data.prediction
X_test= pd.read_csv(Path('brighton-a-memorable-city/testing.csv'), index_col='ID')
X_test=X_test.iloc[:,:4096]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_cv, y_train, y_cv = train_test_split(X, y, test_size = 0.25)

#Fitting RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
features = list(X_train.columns)
classifier = RandomForestClassifier(n_estimators=1000, n_jobs=-1, class_weight='balanced', max_depth=5, max_features="log2")
classifier.fit(X_train,y_train)

y_cv_pred= classifier.predict(X_cv)
y_cv_pred=pd.DataFrame(data =y_cv_pred)
classifier.score(X_cv,y_cv)     
                                                

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

# Predicting the Test set results
y_pred = classifier.predict_proba(X_test)
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

y_pred.to_csv('Inbox/all_data_updown1000_4609feature_maxFeature_log2.csv')
