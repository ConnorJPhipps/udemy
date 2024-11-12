# Generate a linear regrssion model

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load housing data in pandas df
# Cols = Avg. Area Income, Avg. Area Number of Rooms, Avg. Area Number of Bedrooms, Area Population, Price, Address
df = pd.read_csv("Data/USA_Housing.csv")

# Quick pair plot to look at data
'''
sns.pairplot(df)
plt.show()
'''

# Heatmap of correlation of data (drop address bc you can't get a corr for string)
'''
sns.heatmap(df.drop("Address", axis=1).corr())
plt.show()
'''

# Get columns as variables for linear regression
x = df[["Avg. Area Income", "Avg. Area Number of Rooms", "Avg. Area Number of Bedrooms", "Area Population"]]
y = df["Price"]

# Randomly split arrays into train and test datasets with sklearn
# This is done with tuple unpacking
# test_size is percentage of dataset to dedicate to the test dataset
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=101)

# Make an instance of the linear regression model
lm = LinearRegression()

# Fit model on training data
lm.fit(X_train, y_train)

# Evaluate model (intercept and coefficients
print(lm.intercept_)
# print(lm.coef_)
cdf = pd.DataFrame(lm.coef_, x.columns, columns=["Coeff"])
print(cdf)

