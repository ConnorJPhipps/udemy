from locale import normalize

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X = np.arange(10).reshape((5, 2))
y = range(5)

# Splits data into train and test sets (X is features, Y is labels)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Make model and fit to training data
model = LinearRegression()
model.fit(X_train, y_train)

# Predict labels for X_test
predictions = model.predict(X_test)

print(X_test)
print(predictions)