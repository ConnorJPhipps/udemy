import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.pylabtools import figsize
from seaborn import color_palette
# SK learn method to generate blob like groups of data
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
# Make a data set with 200 entries with 2 features with 4 clusters and a std of 1.8 (returns tuple)
data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.8, random_state=101)

# data [0] is features
# data [1] is clusters
#sns.scatterplot(x = data[0][:,0], y = data[0][:,1], hue=data[1])
#plt.show()

kmeans = KMeans(n_clusters=4)
kmeans.fit(data[0])
print(kmeans.cluster_centers_)
# Get labels that K means assigns
print(kmeans.labels_)

# Normally we would not know the labels, but because we do we can compare the assignments to the orig
fig, ax = plt.subplots(1,2, sharey=True, figsize=(10,6))
ax[0].set_title("K Means")
sns.scatterplot(x = data[0][:,0], y = data[0][:,1], hue=kmeans.labels_, ax=ax[0], palette="rainbow")
ax[1].set_title("Orig")
sns.scatterplot(x = data[0][:,0], y = data[0][:,1], hue=data[1], ax=ax[1], palette='rainbow')
plt.show()