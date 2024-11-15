import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Data/Classified Data", index_col=0)
print(df.columns)

# KNN works better with standardized data (z-transformed) (Normalization would remove outliers
scaler = StandardScaler()
# Scale without the classification
scaler.fit(df.drop("TARGET CLASS", axis=1))
# Perform the actual standardization
scaled_features = scaler.transform(df.drop("TARGET CLASS", axis=1))

# Convert scaled features back to a dataframe
df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])

# Train test split
X = df_feat
y = df["TARGET CLASS"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# KNN Time
# Let's start with k=1
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

# Pretty good but is k=1 the best?
# Let's find out using the elbow method
error_rate = []

for num_neighbors in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=num_neighbors)
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    # Average of where predictions were not equal to test values
    # The average of a boolean array is the percentage of error
    error_rate.append(np.mean(predictions != y_test))

# Plot the error_rate and look for cutoffs where the error lowers and stays more consistent
'''
sns.lineplot(error_rate)
plt.show()
'''

# Based off the plot, we should try around 17
knn = KNeighborsClassifier(n_neighbors=17)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))