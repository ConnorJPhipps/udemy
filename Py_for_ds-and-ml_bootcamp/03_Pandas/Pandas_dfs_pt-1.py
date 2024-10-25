# Examples from section 6 of the Python for DS and ML Bootcamp on Udemy
import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

# Initialize df
df = pd.DataFrame(randn(5,4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
print(df)

# Accessing columns
print(df["W"])
print(type(df["W"]))
print(type(df))

# SQL Style columns (Can overwrite df methods)
print(df.W)

# Getting multiple columns (sends back a df)
print(df[["W", "Z"]])

# Generate a new column
df["new"] = df["W"] + df["Y"]
print(df)

# Remove columns (axis 0 is index, axis 1 is columns
# This change does not happen in place (it does not affect df)
df.drop("new", axis=1)
print(df)
# To do change inplace:
df.drop("new", axis=1, inplace=True)
print(df)

# Selecting rows
print(df.loc["A"]) # By index
print(df.iloc[0]) # By index pos

# Getting subsets of rows and cols (row , column)
print(df.loc["B", "Y"])

# Getting multiple vals
print(df.loc[["A", "B"], ["W", "Y"]])
