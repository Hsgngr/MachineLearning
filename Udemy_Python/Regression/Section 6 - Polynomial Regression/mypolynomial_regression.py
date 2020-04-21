# -*- coding: utf-8 -*-

#Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values #Bunun X = dataset.iloc[:, 1].values'dan tek farkı outputun vector değil matrix olarak çıkması.
y = dataset.iloc[:, 2].values

#Fitting linear regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

#Fitting Polynomial Regression to the dataset (This automatically added X0)
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=4) #daha fazla uyması için degreeyi arttır.
X_poly=poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly,y)

#Visualising the Linear Regression results
plt.scatter(X,y, color='red')
plt.plot(X,lin_reg.predict(X), color ='blue')  
plt.title('Truth or Bluff  (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
#Visualising the Polynomial Regression results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X,y, color='red')
plt.plot(X_grid,lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color ='blue')  
plt.title('Truth or Bluff  (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
#Predicting new result with Linear Regression
lin_reg.predict(np.array([6.5]).reshape(1, 1))

#Predicting new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(np.array([6.5]).reshape(1, 1)))
