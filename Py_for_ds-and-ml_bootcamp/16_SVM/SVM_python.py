import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

cancer = load_breast_cancer()

# Learn about dataset
#print(cancer.keys())
#print(cancer["DESCR"])

df_feat = pd.DataFrame(cancer["data"], columns=cancer["feature_names"])
print(df_feat.columns)

X = df_feat
y = cancer["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Train SV classifier
model = SVC()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

# Grid search for best model parameters (What C or Gamma values to use in the model)
#   takes a dict of keys {parameters} and values {what values to test parameters with}
# For SVC:
#   C=cost of misclassification (affects bias/variance tradeoff)
#   gamma=Free param of radial basis function (describes variance in the gaussian distribution)
param_grid = {"C":[0.1, 1, 10, 100, 1000], "gamma":[1, 0.1, 0.01, 0.001, 0.0001]}
grid = GridSearchCV(SVC(), param_grid, verbose=3, refit=True) # Verbose is level of text description
# Run a loop of fits with cross validation for best parameter combination
# Then runs again without cross validation to get best parameter settings to give us the best model
grid.fit(X_train, y_train)
print(grid.best_params_)
print(grid.best_estimator_)
print(grid.best_score_)

grid_predictions = grid.predict(X_test)
print(confusion_matrix(y_test, grid_predictions))
print(classification_report(y_test, grid_predictions))