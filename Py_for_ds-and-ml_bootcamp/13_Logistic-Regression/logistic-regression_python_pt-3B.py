import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_validate

train = pd.read_csv("Data/titanic_train.csv")
first_mean = int(train[train["Pclass"] == 1]["Age"].mean())
second_mean = int(train[train["Pclass"] == 2]["Age"].mean())
thrid_mean =  int(train[train["Pclass"] == 3]["Age"].mean())

def impute_age(cols):
    Age = cols.iloc[0]
    Pclass = cols.iloc[1]
    if pd.isnull(Age):
        if Pclass == 1:
            return first_mean
        elif Pclass == 2:
            return second_mean
        else:
            return thrid_mean # Don't need an elif here because all passenger classes are known
    else:
        return Age # If we already have an age

train["Age"] = train[["Age", "Pclass"]].apply(impute_age, axis=1)
train.drop("Cabin", axis=1, inplace=True)
train.dropna(inplace=True)
pd.get_dummies(train["Sex"])
sex = pd.get_dummies(train["Sex"], drop_first=True) # 1=m, 0=f
embark = pd.get_dummies(train["Embarked"], drop_first=True)
pclass = pd.get_dummies(train["Pclass"], drop_first=True)
pclass.columns = pclass.columns.astype(str)
train = pd.concat([train, sex, embark, pclass], axis=1)
train.drop(["Sex", "Embarked", "Pclass", "Name", "Ticket", "PassengerId"], axis=1, inplace=True)

# We are going to act like the train dataset is all of our data

X = train.drop("Survived", axis=1)
y = train['Survived']

# Split our data into train and test datasets
X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(X, y, test_size=0.3, random_state=101)

from sklearn import  linear_model

# Make our model
log_model = linear_model.LogisticRegression(max_iter=200)

# Train out model
log_model.fit(X_train, y_train)

# Predict from test dataset
predictions = log_model.predict(X_test)

# See how our model did (Evaluation of confusion matrix)
print(sk.metrics.classification_report(y_test, predictions))
print(sk.metrics.confusion_matrix(y_test, predictions))