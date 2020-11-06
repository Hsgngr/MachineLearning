# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:49:52 2020

@author: Ege
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Importing the dataset
dataset=pd.read_csv(Path('imputed_data_with_class_Knn30_headers_upsampled.csv'), index_col=0)
X=dataset.iloc[:, dataset.columns != 'prediction']
y=dataset.prediction
X_test= pd.read_csv(Path('brighton-a-memorable-city/testing.csv'), index_col='ID')

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_cv, y_train, y_cv = train_test_split(X, y, test_size = 0.25, random_state = 5)

#Fitting SVM:
from sklearn.svm import SVC
features = list(X_train.columns)
classifier = SVC(kernel = 'rbf', random_state = 0, gamma=0.1, C=1)
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
###################################################################################################################
#Applying K-Fold cross validation:
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X=X_train,y=y_train, cv=10, n_jobs=-1)
print('Average Accuracy with k-fold cross validation: ' + str(accuracies.mean()))
print('Std:' + str(accuracies.std()))

#Applying Grid Search to Find The Best Model and parameters
from sklearn.model_selection import GridSearchCV
"""
parameters = [{'C': [1,10,100,1000], 'kernel':['linear']},
              {'C': [1,10,100,1000], 'kernel':['rbf'], 'gamma' :[0.5, 0.1, 0.01, 0.001, 0.0001]}]
"""
parameters = {'C': [0.01,0.1,0.5,1], 'kernel':['rbf'], 'gamma' :[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]}

grid_search =GridSearchCV(estimator = classifier, param_grid = parameters, scoring = 'accuracy', cv= 10, n_jobs=-1)  
grid_search = grid_search.fit(X_train, y_train)           

best_accuracy= grid_search.best_score_
best_parameters = grid_search.best_params_
print('Best accuracy: {:.3f}'.format(best_accuracy) )
print('Best parameters: {}'.format(best_parameters) )

##################################################################################################################
#Roc Analization
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
y_cv_pred=classifier.predict(X_cv)
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
y_pred = classifier.predict(X_test)
y_pred=pd.DataFrame(data=y_pred)

#Exporting the results as csv file:

ID=X_test.index.values
y_pred.insert(0,'ID',ID)
y_pred=y_pred.rename(columns={0: 'prediction'})
y_pred.set_index('ID', inplace=True)
y_pred.prediction.value_counts()
y_pred.to_csv('y_pred_upsampled_imputed_with_class_Knn30_RandomForest_balanced_AUC100.csv')

