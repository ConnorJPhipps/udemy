import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

cancer = load_breast_cancer()
#print(cancer.keys())
#print(cancer["DESCR"])

df =pd.DataFrame(cancer["data"], columns=cancer["feature_names"])
print(df.head())

# Scale data to have single unit variance
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

# PCA (you have to determine the number of components to keep)
pca = PCA(n_components=2)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)

# We have now reduced the 30 column dataset into 2 components
print(scaled_data.shape)
print(x_pca.shape)

#sns.scatterplot(x=x_pca[:,0], y=x_pca[:,1], hue=cancer["target"])
#plt.show()

# Let's explore the components and how they related to the orig data/features
# pca.components_ represents the correlation of the component with the features
df_comp = pd.DataFrame(pca.components_, columns=cancer["feature_names"])
sns.heatmap(df_comp, cmap="plasma")
plt.show()