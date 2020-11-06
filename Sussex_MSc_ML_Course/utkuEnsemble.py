# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:37:52 2020

@author: Ege
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score, roc_curve, auc
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
import gc
from pathlib import Path

class Ensemble:

    # Takes in learners and ensemblers and holds them as fields
    def __init__(self, learners, ensemblers):
        self.learners = learners
        self.ensemblers = ensemblers
        self.learner_accuracies = dict()
        self.learner_aurocs = dict()

    # Trains the learners on the given data
    def train_learners(self, X, y):
        for key in self.learners.keys():
            self.learners[key].fit(X, y)

    # Trains the ensemblers with the predictions taken from the given dataset using learners.
    def train_ensemblers(self, X, y):
        preds = self.take_predictions_from_learners(X=X, y=y, verbose=True)
        self.print_learner_accuracy_on_training_data()
        self.print_learner_auroc_on_training_data()
        for key in self.ensemblers.keys():
            self.ensemblers[key].fit(preds, y)

    # Makes predictions on the given dataset according to the ensemblers
    def predict(self, X):
        preds = self.take_predictions_from_learners(X)
        predictions = dict()
        for key in self.ensemblers:
            predictions[key] = self.ensemblers[key].predict(preds)
        return predictions

    # Takes predictions from learners and concatenates them
    def take_predictions_from_learners(self, X, y=None, verbose=False):
        probs = []
        for key in self.learners.keys():
            prob = self.learners[key].predict_proba(X)[:, 1]
            prediction = self.learners[key].predict(X)
            if verbose:
                self.learner_accuracies[key] = calculate_accuracy(y, prediction)
                self.learner_aurocs[key] = calculate_auroc(y, prob)
            probs.append(prob[:, np.newaxis])
        return np.concatenate(probs, axis=1)

    # Takes predictions from the given ensembler with the given dataset
    def predict_with_given_ensembler(self, X, ensembler):
        preds = self.take_predictions_from_learners(X)
        return self.ensemblers[ensembler].predict(preds)

    # Takes predictions from the given ensembler with the given dataset
    def predict_proba_with_given_ensembler(self, X, ensembler):
        preds = self.take_predictions_from_learners(X)
        return self.ensemblers[ensembler].predict_proba(preds)[:, 1]

    # Returns the prediction probability of the positive class
    def predict_proba(self, X):
        preds = self.take_predictions_from_learners(X)
        predictions = dict()
        for key in self.ensemblers:
            predictions[key] = self.ensemblers[key].predict_proba(preds)[:, 1]
        return predictions

    # Prints the accuracy of learners on the training data
    def print_learner_accuracy_on_training_data(self):
        for key in self.learner_accuracies.keys():
            print('Accuracy for learner {} is: {}'.format(key, self.learner_accuracies[key]))
        print()

    # Prints the aurocs for learners on the training data
    def print_learner_auroc_on_training_data(self):
        for key in self.learner_aurocs.keys():
            print('Auroc for learner {} is: {}'.format(key, self.learner_aurocs[key]))
        print()


def calculate_accuracy(true, preds):
    return accuracy_score(true, preds)


# Calculates the Area Under The Receiving
def calculate_auroc(true, preds):
    return roc_auc_score(true, preds)


# Creates a confusion matrix where true_labels are on the first dimension
def find_confusion_matrix(y_true, y_pred, class_labels):
    num_class = class_labels.shape[0]
    confusion_matrix = np.zeros((num_class, num_class))
    for i, j in zip(y_true.astype('int64'), y_pred.astype('int64')):
        confusion_matrix[i, j] += 1
    return confusion_matrix.astype(int)


# Prints the confusion matrix defined as above
def print_confusion_matrix(confusion_matrix, class_labels):
    print('\ty_hat')
    print('y_test\t\t', end='')
    [print('{}\t'.format(i), end='') for i in class_labels.astype('int64')]
    print()
    for i in np.arange(confusion_matrix.shape[0]):
        print('\t{}'.format(i), end='')
        for j in np.arange(confusion_matrix.shape[0]):
            print('\t{}'.format(confusion_matrix[i, j]), end='')
        print()


# Drops if a column's 60% is NaN and fills the remaining nans with mean if numerical mode if categorical.
def prepare_data_simple_imputer(df):
    cols = drop_na_cols(df, 0.6)
    numerical_vals = df.select_dtypes(['int64', 'float64'])
    numerical_imputer = SimpleImputer(strategy='mean')
    X = numerical_imputer.fit_transform(numerical_vals)
    categorical_vals = df.select_dtypes('object')
    categorical_imputer = SimpleImputer(strategy='most_frequent')
    categorical_vals = categorical_imputer.fit_transform(categorical_vals)
    ohe = OneHotEncoder(categories='auto')
    categorical_vals_encoded = None
    if categorical_vals.shape != 0:
        categorical_vals_encoded = ohe.fit_transform(categorical_vals).toarray()
    if categorical_vals_encoded is not None:
        X = np.concatenate((X, categorical_vals_encoded), axis=1)
    return cols, X


def drop_na_cols(df, rate):
    dropped_cols = []
    for col in df.columns:
        num_missing_value = df[col].isnull().sum()
        if num_missing_value / len(df[col]) > rate:
            df.drop(columns=col, inplace=True)
            dropped_cols.append(col)
    return np.array(dropped_cols)


def prepare_data(df):
    cols = drop_na_cols(df, 0)
    X = df.select_dtypes(['int64', 'float64']).values
    categorical_vals = df.select_dtypes('object')
    ohe = OneHotEncoder(categories='auto')
    categorical_vals_encoded = None
    if not categorical_vals.empty:
        categorical_vals_encoded = ohe.fit_transform(categorical_vals).toarray()
    if categorical_vals_encoded is not None:
        X = np.concatenate((X, categorical_vals_encoded), axis=1)
    return cols, X


def extract_not_nan_labels(df_X, df_y):
    target_samples = []
    for target in df_labels.columns:
        X = df_X[~df_y[target].isnull()].values
        y = df_y[~df_y[target].isnull()][target].values[:, np.newaxis]
        target_samples.append(np.concatenate((X, y), axis=1))
    return target_samples


def extract_nan_labels(df_X, df_y):
    target_samples = []
    for target in df_labels.columns:
        X = df_X[df_y[target].isnull()].values
        target_samples.append(X)
    return target_samples


def prediction_results(true, preds, probs):
    class_labels = np.unique(true)
    best_fpr = None
    best_tpr = None
    best_acc = 0
    best_auroc = 0
    best_ensembler = None
    best_cm = None
    for predictor in preds.keys():
        curr_probs = probs[predictor]
        curr_preds = preds[predictor]
        fpr, tpr, thresholds = roc_curve(true, curr_probs)
        auroc = auc(fpr, tpr)
        if auroc > best_auroc:
            best_auroc = auroc
            best_ensembler = predictor
            best_fpr = fpr
            best_tpr = tpr
            best_acc = calculate_accuracy(true, curr_preds)
            best_cm = find_confusion_matrix(true, curr_preds, class_labels)

    print_confusion_matrix(best_cm, class_labels)
    print('Accuracy for the best ensembler {} is {}'.format(best_ensembler, best_acc))
    plt.plot(best_fpr, best_tpr)
    plt.xlabel('FP Rate')
    plt.ylabel('TP Rate')
    plt.title('Receiver Operating Characteristic for {}'.format(best_ensembler))
    plt.show()
    print('AUROC for the best ensembler {} is {}'.format(best_ensembler, best_auroc))

    return best_ensembler


def split_to_data_and_label(targets):
    data_and_label = []
    for target in targets:
        data_and_label.append((target[:, :-1], target[:, -1]))
    return data_and_label


def results(true, preds, probs, best_ensembler):
    class_labels = np.unique(true)
    fpr, tpr, thresholds = roc_curve(true, probs)
    auroc = auc(fpr, tpr)
    print_confusion_matrix(find_confusion_matrix(true, preds, class_labels), class_labels)
    print('Accuracy for the best ensembler {} is {}'.format(best_ensembler, calculate_accuracy(true, preds)))
    plt.plot(fpr, tpr)
    plt.xlabel('FP Rate')
    plt.ylabel('TP Rate')
    plt.title('Receiver Operating Characteristic for {}'.format(best_ensembler))
    plt.show()
    print('AUROC for the best ensembler {} is {}'.format(best_ensembler, auroc))
    

# Importing the dataset
dataset=pd.read_csv(Path('imputed_data_with_class_Knn30_headers_upsampled.csv'), index_col=0)
X_training=dataset.iloc[:, dataset.columns != 'prediction'].values
y=dataset.prediction.values;
#X_training = pd.read_csv('all_X.csv', index_col=0).values
#num_training = X_training.shape[0]
#y = pd.read_csv('all_labels.csv', index_col=0)    
X_test= pd.read_csv(Path('brighton-a-memorable-city/testing.csv'), index_col='ID')
num_test = X_test.shape[0]


X_train_target, X_test_target, y_train_target, y_test_target = train_test_split(X_training, y,
                                                                                        test_size=0.1,
                                                                                        stratify=y)
X_train_target, X_val_target, y_train_target, y_val_target = train_test_split(X_train_target, y_train_target,
                                                                                      test_size=3 / 9,
                                                                                      stratify=y_train_target)

learners = dict()
ensemblers = dict()
learners['RandomForestClassifier'] = RandomForestClassifier(n_estimators=1000, n_jobs=6)
learners['GradientBoostingClassifier'] = GradientBoostingClassifier(n_estimators=100, criterion='mse')
learners['XGBClassifier'] = XGBClassifier(objective='binary:logistic', n_estimators=1000, n_jobs=6)
#learners['MLPClassifier'] = MLPClassifier(activation='relu', solver='sgd')
learners['LogisticRegression'] = LogisticRegression(solver='lbfgs', max_iter=2000)
ensemblers['LogisticRegressionEnsembler'] = LogisticRegression(solver='lbfgs', max_iter=1000)
ensemblers['GradientBoostingClassifierEnsembler'] = GradientBoostingClassifier(n_estimators=100,
                                                                                       criterion='mse')
ensemblers['XGBClassifierEnsembler'] = XGBClassifier(n_estimators=100, objective='binary:logistic',
                                                             n_jobs=6)
ensemblers['RandomForestClassifierEnsembler'] = RandomForestClassifier(n_estimators=100, n_jobs=6)
ensemblers['MLPClassifier'] = MLPClassifier(activation='logistic', solver='sgd', max_iter=1000)

ensembler = Ensemble(learners, ensemblers)
ensembler.train_learners(X_train_target, y_train_target)
ensembler.train_ensemblers(X_val_target, y_val_target)

#############################################################################################################################

X_test=X_test.values
prediction_matrix = ensembler.predict(X_test)

X_test=pd.DataFrame(data = X_test)
y_pred= pd.DataFrame(prediction_matrix['MLPClassifier'])

X_test= pd.read_csv(Path('brighton-a-memorable-city/testing.csv'))
ID=X_test.iloc[:,0].values

y_pred.insert(0,'ID',ID)
y_pred=y_pred.rename(columns={0: 'prediction'})
y_pred.set_index('ID', inplace=True)
y_pred.to_csv('y_pred_upsampled_data_MLP_new.csv')


y_pred=pd.DataFrame(data=np.ones(num_test).astype('int64'))
y_pred=y_pred.rename(columns={1: 'prediction'})

