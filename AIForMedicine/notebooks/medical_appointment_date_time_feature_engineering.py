# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 23:42:58 2020

@author: Ege

A great tutorial Datetime Feature Engineering: 
https://towardsdatascience.com/machine-learning-with-datetime-feature-engineering-predicting-healthcare-appointment-no-shows-5e4ca3a85f96

"""

#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#Data Preparation
df = pd.read_csv(Path('KaggleV2-May-2016.csv'))

#Investigate the No-Show column with value_counts
df['No-show'].value_counts()

'''
No     88208
Yes    22319
'''
#Create a column as changing the Yes/No column to the binary
df['OUTPUT_LABEL'] = (df['No-show'] == 'Yes').astype('int')

#Show the distribution of the label as a ratio
def calc_prevalence(y):
 return (sum(y)/len(y))

calc_prevalence(df.OUTPUT_LABEL.values)
'''
>>> 0.20193255946510807

which means that 1 in 5 patients will miss their scheduled appointment.
'''

#Investigate the date column
df.ScheduledDay.head()

'''
0    2016-04-29T18:38:08Z
1    2016-04-29T16:08:27Z
2    2016-04-29T16:19:04Z
3    2016-04-29T17:29:31Z
4    2016-04-29T16:07:23Z
Name: ScheduledDay, dtype: object

'''
#Format the date data with pd.to_datetime function
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'], 
 format = '%Y-%m-%dT%H:%M:%SZ', 
 errors = 'coerce')
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'], 
 format = '%Y-%m-%dT%H:%M:%SZ', 
 errors = 'coerce')

'''
0   2016-04-29 18:38:08
1   2016-04-29 16:08:27
2   2016-04-29 16:19:04
3   2016-04-29 17:29:31
4   2016-04-29 16:07:23
Name: ScheduledDay, dtype: datetime64[ns]
'''

#Test if the format is correct
assert df.ScheduledDay.isnull().sum() == 0, 'missing ScheduledDay dates'
assert df.AppointmentDay.isnull().sum() == 0, 'missing AppointmentDay dates'


#One thing I noticed was that currently there are ~40k appointments 
#that were scheduled after the appointment datetime.
(df['ScheduledDay'] > df['AppointmentDay']).sum() #38568 appointment is in wrong schedule.

df['AppointmentDay']  = df['AppointmentDay'] +  pd.Timedelta('1d') -pd.Timedelta('1s')
'''
0   2016-04-29 23:59:59
1   2016-04-29 23:59:59
2   2016-04-29 23:59:59
3   2016-04-29 23:59:59
4   2016-04-29 23:59:59
Name: AppointmentDay, dtype: datetime64[ns]
'''

#There is only 5 rows left where scheduledDay time is after appointmentDay. Lets just drop those rows
(df['ScheduledDay'] > df['AppointmentDay']).sum()

df = df.loc[(df['ScheduledDay'] <= df['AppointmentDay'])].copy()

## Engineer date-time features
df['ScheduledDay_year'] = df['ScheduledDay'].dt.year
df['ScheduledDay_month'] = df['ScheduledDay'].dt.month
df['ScheduledDay_week'] = df['ScheduledDay'].dt.week
df['ScheduledDay_day'] = df['ScheduledDay'].dt.day
df['ScheduledDay_hour'] = df['ScheduledDay'].dt.hour
df['ScheduledDay_minute'] = df['ScheduledDay'].dt.minute
df['ScheduledDay_dayofweek'] = df['ScheduledDay'].dt.dayofweek
df['AppointmentDay_year'] = df['ScheduledDay'].dt.year
df['AppointmentDay_month'] = df['AppointmentDay'].dt.month
df['AppointmentDay_week'] = df['AppointmentDay'].dt.week
df['AppointmentDay_day'] = df['AppointmentDay'].dt.day
df['AppointmentDay_hour'] = df['AppointmentDay'].dt.hour
df['AppointmentDay_minute'] = df['AppointmentDay'].dt.minute
df['AppointmentDay_dayofweek'] = df['AppointmentDay'].dt.dayofweek


#You can verify this work:
df_verify= df[['ScheduledDay', 'ScheduledDay_year', 'ScheduledDay_month','ScheduledDay_week',
    'ScheduledDay_day','ScheduledDay_hour','ScheduledDay_minute','ScheduledDay_dayofweek']].head()

#At this point it would be good to explore our dates a bit:
df.groupby('AppointmentDay_year').size()
'''
AppointmentDay_year
2015        62
2016    110460
dtype: int64

'''
df.groupby('AppointmentDay_month').size()

'''
AppointmentDay_month
4     3235
5    80836
6    26451
dtype: int64
'''

df.groupby('AppointmentDay_dayofweek').size()
'''
AppointmentDay_dayofweek
0    22714
1    25638
2    25866
3    17246
4    19019
5       39
dtype: int64
'''
#Let's check if dayofwork is predictive of no-show:
df.groupby('AppointmentDay_dayofweek').apply(lambda g: calc_prevalence(g.OUTPUT_LABEL.values))

'''
Looks like more people skip their appointments on Friday and Saturday, although the effect is modest.
'''
#Let's create a new feature that is the number of days between the scheduled date and the appointment date.

df['delta_days'] = (df['AppointmentDay']-df['ScheduledDay']).dt.total_seconds()/(60*60*24)

#Plot the histogram of our two classes on this variable:

plt.hist(df.loc[df.OUTPUT_LABEL == 1,'delta_days'], 
 label = 'Missed',bins = range(0,60,1), normed = True)

plt.hist(df.loc[df.OUTPUT_LABEL == 0,'delta_days'], 
 label = 'Not Missed',bins = range(0,60,1), normed = True,alpha =0.5)

plt.legend()
plt.xlabel('days until appointment')
plt.ylabel('normed distribution')
plt.xlim(0,40)
plt.show()

'''
This distribution is a bit odd to me since most of the patients 
who did not miss their appointment cheduled the appointment on the same day.
 I kind of wonder if walk-in appointments are included in this data set.
 My guess is that this model will just draw a line at 1 day and 
 say not-missed if you scheduled it the same day.
'''

#Split the Dataset
# shuffle the samples
df = df.sample(n = len(df), random_state = 42)
df = df.reset_index(drop = True)
df_valid = df.sample(frac = 0.3, random_state = 42)
df_train = df.drop(df_valid.index)

#Check if the split is homogeneous
print('Valid prevalence(n = %d):%.3f'%(len(df_valid),calc_prevalence(df_valid.OUTPUT_LABEL.values)))
print('Train prevalence(n = %d):%.3f'%(len(df_train), calc_prevalence(df_train.OUTPUT_LABEL.values)))

'''
Valid prevalence(n = 33157):0.201
Train prevalence(n = 77365):0.202
'''

col2use = ['ScheduledDay_day', 'ScheduledDay_hour',
 'ScheduledDay_minute', 'ScheduledDay_dayofweek', 
 'AppointmentDay_day',
 'AppointmentDay_dayofweek', 'delta_days']

# We can now build our X (inputs) and Y(output) for training and validation:
X_train = df_train[col2use].values
X_valid = df_valid[col2use].values
y_train = df_train['OUTPUT_LABEL'].values
y_valid = df_valid['OUTPUT_LABEL'].values
print('Training shapes:',X_train.shape, y_train.shape)
print('Validation shapes:',X_valid.shape, y_valid.shape)

#Train simple random-forest-model
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(max_depth = 5, n_estimators=100, random_state = 42)
rf.fit(X_train, y_train)

# We can then get our predictions with:
y_train_preds = rf.predict_proba(X_train)[:,1]
y_valid_preds = rf.predict_proba(X_valid)[:,1]


##Evaluation Metrics
from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score
def calc_specificity(y_actual, y_pred, thresh):
 # calculates specificity
 return sum((y_pred < thresh) & (y_actual == 0)) /sum(y_actual ==0)
def print_report(y_actual, y_pred, thresh):
 
 auc = roc_auc_score(y_actual, y_pred)
 accuracy = accuracy_score(y_actual, (y_pred > thresh))
 recall = recall_score(y_actual, (y_pred > thresh))
 precision = precision_score(y_actual, (y_pred > thresh))
 specificity = calc_specificity(y_actual, y_pred, thresh)
 print('AUC:%.3f'%auc)
 print('accuracy:%.3f'%accuracy)
 print('recall:%.3f'%recall)
 print('precision:%.3f'%precision)
 print('specificity:%.3f'%specificity)
 print('prevalence:%.3f'%calc_prevalence(y_actual))
 print(' ')
 return auc, accuracy, recall, precision, specificity

'''
Using this print_report function we can evaluate the performance for training and validation.
'''
thresh= 0.201

print('Random Forest')
print('Training')
print_report(y_train, y_train_preds, thresh)
print('Validation')
print_report(y_valid, y_valid_preds, thresh)

'''
Random Forest
Training
AUC:0.720
accuracy:0.519
recall:0.920
precision:0.286
specificity:0.418
prevalence:0.202

Validation
AUC:0.711
accuracy:0.519
recall:0.918
precision:0.284
specificity:0.418
prevalence:0.201

'''

#Lets Plot the ROC curve:
from sklearn.metrics import roc_curve
fpr_train, tpr_train, thresholds_train = roc_curve(y_train, y_train_preds)
auc_train = roc_auc_score(y_train, y_train_preds)
fpr_valid, tpr_valid, thresholds_valid = roc_curve(y_valid, y_valid_preds)
auc_valid = roc_auc_score(y_valid, y_valid_preds)
plt.plot(fpr_train, tpr_train, 'r-',label ='Train AUC:%.3f'%auc_train)
plt.plot(fpr_valid, tpr_valid, 'b-',label ='Valid AUC:%.3f'%auc_valid)
plt.plot([0,1],[0,1],'--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()    


##Future Importance
feature_importances = pd.DataFrame(rf.feature_importances_,
index = col2use,
columns=['importance']).sort_values('importance',
ascending=False)
num = min([50,len(col2use)])
ylocs = np.arange(num)
# get the feature importance for top num and sort in reverse order
values_to_plot = feature_importances.iloc[:num].values.ravel()[::-1]
feature_labels = list(feature_importances.iloc[:num].index)[::-1]
plt.figure(num=None, figsize=(6, 6), dpi=80, facecolor='w', edgecolor='k');
plt.barh(ylocs, values_to_plot, align = 'center')
plt.ylabel('Features')
plt.xlabel('Importance Score')
plt.title('Feature Importance Score — Random Forest')
plt.yticks(ylocs, feature_labels)
plt.show()

'''
Which shows that delta_days is basically the only features used in the model. 
This confirms our suspicion above that the model will 
likely struggle due to those same day appointments.
'''

'''
Since our training and validation scores are very similar,
 this means that we are in the case of high bias. 
 In order to improve this model, we will need additional features,
 so I will end this project here.
'''

