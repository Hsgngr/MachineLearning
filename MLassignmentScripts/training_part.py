"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 15:33 11.04.202
"""
#Logistic Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Importing the dataset
X = pd.read_csv('all_X.csv', index_col=0)
y = pd.read_csv('all_labels.csv', index_col=0)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_cv, y_train, y_cv = train_test_split(X, y, test_size = 0.25, random_state = 0)

#Fitting RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
features = list(X_train.columns)
classifier = RandomForestClassifier(n_estimators=1000, n_jobs=-1, class_weight={0:1,1:0.75})
classifier.fit(X_train,y_train)

y_cv_pred= classifier.predict(X_cv)
y_cv_pred=pd.DataFrame(data =y_cv_pred)
classifier.score(X_cv,y_cv)     

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

y_cv_pred= classifier.predict(X_cv)
y_cv_pred=pd.DataFrame(data =y_cv_pred)
classifier.score(X_cv,y_cv)                                                    #Bunu yaptığımızda y_cv_prediction'ı koymamıza gerek yok o zaman içinde internally predictionu yapıyor.

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
X_test= pd.read_csv(Path('brighton-a-memorable-city/testing.csv'))

# Predicting the Test set results
y_pred = classifier.predict(X_test)

#Exporting the results as csv file:
y_pred=pd.DataFrame(data=y_pred)
ID=X_test.iloc[:,0].values
y_pred.insert(0,'ID',ID)
y_pred=y_pred.rename(columns={0: 'prediction'})
y_pred.set_index('ID', inplace=True)
y_pred.to_csv('y_pred.csv')

