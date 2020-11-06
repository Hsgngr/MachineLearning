

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 01:12:51 2020

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

#Fitting RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
features = list(X_train.columns)
classifier = RandomForestClassifier(n_estimators=20, n_jobs=-1, class_weight='balanced',max_features = 'sqrt')
classifier.fit(X_train,y_train)

y_cv_pred= classifier.predict(X_cv)
y_cv_pred=pd.DataFrame(data =y_cv_pred)
classifier.score(X_cv,y_cv)                                              #Bunu yaptığımızda y_cv_prediction'ı koymamıza gerek yok o zaman içinde internally predictionu yapıyor.

########################################################################################################          
#Feature Selection

fi = pd.DataFrame({'feature': list(X_train.columns),
                   'importance': classifier.feature_importances_}).\
                    sort_values('importance', ascending = False)
                    
from sklearn.feature_selection import SelectFromModel                    
sfm = SelectFromModel(classifier, threshold=0.0007)

# Train the selector
sfm.fit(X_train, y_train)
#Select most important features
X_important_train = sfm.transform(X_train)
X_important_cv = sfm.transform(X_cv)
X_important_test = sfm.transform(X_test)
###########################################3
from sklearn.metrics import roc_curve, auc
n_estimators = [1, 2, 4, 8, 16, 32, 64, 100, 200]
train_results = []
test_results = []
for estimator in n_estimators:
    rf = RandomForestClassifier(n_estimators=estimator, n_jobs=-1)
    rf.fit(X_important_train, y_train)
    train_pred = rf.predict(X_important_train)
    false_positive_rate, true_positive_rate, thresholds = roc_curve(y_train, train_pred)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    train_results.append(roc_auc)
    y_pred = rf.predict(X_important_cv)
    false_positive_rate, true_positive_rate, thresholds = roc_curve(y_cv, y_pred)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    test_results.append(roc_auc)
    
# Create a new random forest classifier for the most important features
clf_important = RandomForestClassifier(n_estimators=1000, random_state=0, n_jobs=-1, max_depth=5)

# Train the new classifier on the new dataset containing the most important features
clf_important.fit(X_important_train, y_train)

#
y_cv_pred= clf_important.predict(X_important_cv)
y_cv_pred=pd.DataFrame(data =y_cv_pred)
clf_important.score(X_important_cv,y_cv)   
###############################################################################################################
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
y_pred = clf_important.predict_proba(X_important_test)
threshold=0.4849
y_pred [:,0] = (y_pred [:,0] < threshold).astype('int')
y_pred=pd.DataFrame(data=y_pred)
y_pred = y_pred.astype('int')
y_pred.drop(columns=[1], inplace=True)

# Predicting the Test set results
y_pred = classifier.predict_proba(X_test)
threshold=0.3
y_pred [:,0] = (y_pred [:,0] < threshold).astype('int')
y_pred=pd.DataFrame(data=y_pred)
y_pred = y_pred.astype('int')
y_pred.drop(columns=[1], inplace=True)

#Exporting the results as csv file:

ID=X_test.index.values
y_pred.insert(0,'ID',ID)
y_pred=y_pred.rename(columns={0: 'prediction'})
y_pred.set_index('ID', inplace=True)
y_pred.prediction.value_counts()

y_pred.to_csv('y_pred_upsampled_RandomForest2_with_threshold_4849.csv')

