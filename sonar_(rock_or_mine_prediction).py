# -*- coding: utf-8 -*-
"""SONAR (Rock or Mine Prediction).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/122LAU_eGhRHlYrgcUc2PTfjBVknZ1d4T

Importing the Required Libraries
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Processing"""

# Load the dataset into a pandas dataframe
# header=None beacuse there are no labels for our columns in the Dataset
sonar_data = pd.read_csv('/content/sonar_data.csv', header=None)

sonar_data.head()

sonar_data.tail()

# Number of Rows and Columns in our DataFrame
sonar_data.shape

# Getting Statistical Measue for our Data
sonar_data.describe()

"""M -> Mine
R -> Rock
"""

# Getting Number of Rocks & Mines samples
sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

# Seperating Data & Labels
X = sonar_data.drop(columns = 60, axis = 1) # axis = 1 because We are dropping a column
Y = sonar_data[60]

print(X)
print(Y)

"""Splitting the Data into Training & Test Data"""

# stratify=Y is to split data into equal proportions of Rocks & Mines in
# both training as well as the test data.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state = 1)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training using Logistic Regression"""

model = LogisticRegression()

# Training the Logistic Regression Model with the training data
model.fit(X_train, Y_train)

"""Model Evaluation using accuracy score"""

# accuracy on the training data
# Accuracy of more than 70% is generally good
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print(training_data_accuracy)

print("Accuracy for the training data : ", training_data_accuracy)

# accuracy on the test data
# Accuracy of more than 70% is generally good
X_test_prediction = model.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print("Accuracy for the testing data : ", testing_data_accuracy)

"""Making a Predictive System"""

# This input data is for a Mine
input_data = (0.0629,0.1065,0.1526,0.1229,0.1437,0.1190,0.0884,0.0907,0.2107,0.3597,0.5466,0.5205,0.5127,0.5395,0.6558,0.8705,0.9786,0.9335,0.7917,0.7383,0.6908,0.3850,0.0671,0.0502,0.2717,0.2839,0.2234,0.1911,0.0408,0.2531,0.1979,0.1891,0.2433,0.1956,0.2667,0.1340,0.1073,0.2023,0.1794,0.0227,0.1313,0.1775,0.1549,0.1626,0.0708,0.0129,0.0795,0.0762,0.0117,0.0061,0.0257,0.0089,0.0262,0.0108,0.0138,0.0187,0.0230,0.0057,0.0113,0.0131)

# changing the input_data to a numpy array for faster computations
input_data_as_np_array = np.asarray(input_data)

# Reshape the numpy array as we are predicting for only 1 instance
# Note: The short version: we can only use predict on data that is of the same dimensionality as the training data (X) was.
# In the example in question, we give the computer a bunch of rows in X (with 60 values each) and we show it the correct responses in y. 
# When we want to predict using new values, our program expects the same - a bunch of rows. Even if we want to do it to just one row 
# (with 60 values), that row has to be part of another 2D array to do this we use .reshape(1,-1)
input_data_reshaped = input_data_as_np_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)

if(prediction[0] == 'M'):
  print("Prediction is a Mine")
else:
  print("Prediction is a Rock")