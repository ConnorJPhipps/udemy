import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv("Data/titanic_train.csv")

#sns.boxplot(x="Pclass", y='Age', data=train, hue="Pclass")
#plt.show()


# We are missing some ages due to NAs (~20), lets impute them using other KNOWN data
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

# Check if NA's are gone for "Age" column
'''
null_arr = train.isnull() # Get boolean array with True for null values
sns.heatmap(null_arr, yticklabels=False, cbar=False, cmap="viridis")
plt.show()
'''

# Unlike "Age", "Cabin" is missing too much data to impute/be useful so we should drop it
train.drop("Cabin", axis=1, inplace=True)

# Drop remaining missing values
train.dropna(inplace=True)

# Now we have to convert categorical vars into vars usable by our ml algorithms (make dummy variables)
pd.get_dummies(train["Sex"])
# This would give us 2 cols, 1 where f=1 and m=0 and the other the inverse
# This would cause multicollinearity as one col would perfectly predict the other (We only need to save one)
sex = pd.get_dummies(train["Sex"], drop_first=True) # 1=m, 0=f

# Embark would give us three columns so again we must drop the first to avoid multicollinearity
embark = pd.get_dummies(train["Embarked"], drop_first=True)

# The dropped columns essentially become the reference columns in the case of embarked so we aren't actually losing data
train = pd.concat([train, sex, embark], axis=1)

# Drop columns we are not planning on using (name and ticket number likely do not have predictive values)
# We also need to drop the columns we turned into dummy variables
train.drop(["Sex", "Embarked", "Name", "Ticket", "PassengerId"], axis=1, inplace=True)
print(train)