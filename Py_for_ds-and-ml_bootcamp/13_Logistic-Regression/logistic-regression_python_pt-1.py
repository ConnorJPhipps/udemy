import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv("Data/titanic_train.csv")
# Columns = PassengerID, Survived, Pclass, Name, Sex, Age, SibSP, Parch, Ticket, Fare, Cabin, Embarked
#   SibSP = number of siblings/spouses; Parch = number of parents and children on board

# Make a heat map with seaborn to identify missing data
null_arr = train.isnull() # Get boolean array with True for null values
'''
sns.heatmap(null_arr, yticklabels=False, cbar=False, cmap="viridis")
plt.show()
'''
# We can see we are missing about 20% of age (little enough to use replacement with imputation/infer from other cols_
# Cabin however is nearly entirely missing

sns.set_style("whitegrid")

# Look at some proportions in the data
#sns.countplot(x="Survived", data=train)
#sns.countplot(x="Survived", data=train, hue="Sex", palette="RdBu_r")
#sns.countplot(x="Survived", data=train, hue="Pclass")
#sns.displot(train['Age'].dropna(), kde=False, bins=30)
#sns.countplot(x="SibSp", data=train)
sns.displot(x="Fare", data=train, bins=40)
plt.show()
