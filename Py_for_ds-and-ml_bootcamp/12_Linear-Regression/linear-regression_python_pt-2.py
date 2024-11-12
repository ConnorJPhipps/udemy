import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Make linear regression model from part 2
df = pd.read_csv("Data/USA_Housing.csv")
x = df[["Avg. Area Income", "Avg. Area Number of Rooms", "Avg. Area Number of Bedrooms", "Area Population"]]
y = df["Price"]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=101)
lm = LinearRegression()
lm.fit(X_train, y_train)

# Use model on test set (features only)
predictions = lm.predict(X_test)

# Look at predicted house prices and correct prices of the house
#print(predictions)
#print(y_test)

# Assess fit with a scatter plot
'''
sns.scatterplot(x=y_test, y=predictions)
plt.show()
'''

# Look at residuals (diff between actual and predicted)
# In our case the residuals are normally distributed (indicative of our model being a good choice for the data)
'''
sns.displot((y_test-predictions))
plt.show()
'''

# Evaluation metrics for model
#   Mean absolute error (MAE)
#   Mean squared error (MSE)
#   Root mean squared error (RMSE)

MAE = metrics.mean_absolute_error(y_test, predictions)
MSE = metrics.mean_squared_error(y_test, predictions)
RMSE = metrics.root_mean_squared_error(y_test, predictions) # Could also do sqrt of MSE
print(f"MAE: {MAE:.2f}\nMSE: {MSE:.2f}\nRMSE: {RMSE:.2f}")