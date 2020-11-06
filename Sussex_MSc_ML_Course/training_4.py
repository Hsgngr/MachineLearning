# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:02:50 2020

@author: Ege
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


# Importing the dataset
dataset=pd.read_csv(Path('Imbalanced_data/data_upsammpled.csv'), index_col=0)
X=dataset.iloc[:,:4096]
y=dataset.prediction
X_test= pd.read_csv(Path('brighton-a-memorable-city/testing.csv'), index_col='ID')
X_test=X_test.iloc[:,:4096]
#######################################################################################################################
#Feature Selection
from feature_selector import FeatureSelector

fs = FeatureSelector(data = X, labels = y)
fs.identify_collinear(correlation_threshold = 0.9)
collinear_features = fs.ops['collinear']

# Pass in the appropriate parameters
fs.identify_zero_importance(task = 'classification', 
                            eval_metric = 'auc', 
                            n_iterations = 10, 
                             early_stopping = True)
# list of zero importance features
zero_importance_features = fs.ops['zero_importance']

# plot the feature importances
fs.plot_feature_importances(threshold = 0.95, plot_n = 20)

fs.identify_low_importance(cumulative_importance = 0.95)

# Remove the features from all methods (returns a df)
train_removed = fs.remove(methods = 'all')
train_removed, X_test = train_removed.align(X_test, axis=1, join='inner') #Test datasının 
######################################################################################################################
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_cv, y_train, y_cv = train_test_split(train_removed, y, test_size = 0.25)

#Fitting RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
features = list(X_train.columns)
classifier = RandomForestClassifier(n_estimators=1000, n_jobs=-1, class_weight='balanced_subsample')
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

# Predicting the Test set results
y_pred = classifier.predict_proba(X_test)
threshold=0.468
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

y_pred.to_csv('y_pred_upsampled_RandomForest2_with_threshold435_featureSelector_3103.csv')
