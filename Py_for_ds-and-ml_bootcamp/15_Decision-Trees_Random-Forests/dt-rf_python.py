import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Data/kyphosis.csv")
# Kyphosis=Presence after intervention, Age=age in mo.
# Number=num vertebrae in intervention, Start=Top vertebrae in intervention
print(df.head())

# Quick look at data
'''
sns.pairplot(df, hue="Kyphosis")
plt.show()
'''

# Split data into tran and test
X = df.drop("Kyphosis", axis=1)
y = df["Kyphosis"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Train a single decision tree
d_tree = DecisionTreeClassifier()
d_tree.fit(X_train, y_train)
predictions = d_tree.predict(X_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

# Random forest model (with 200 trees)
r_forest = RandomForestClassifier(n_estimators=200)
r_forest.fit(X_train, y_train)
predictions = r_forest.predict(X_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))