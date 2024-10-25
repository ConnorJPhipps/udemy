# Examples from section 6 of the Python for DS and ML Bootcamp on Udemy
import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame({"col1": [1, 2, 3, 4],
                   "col2": [444, 555, 666, 444],
                   "col3": ["abc", "def", "ghi", "xyz"]})
print(df)

# Find unique values in a df
print(df["col2"].unique())
print(len(df["col2"].unique()))
print(df["col2"].nunique())

# Find values counts
print(df["col2"].value_counts())

# Apply allows you to use functions on pandas series
def times2(x):
    return x*2

print(df["col1"].apply(times2))
print(df["col2"].apply(lambda x: x*2))

# remove columns
print(df.drop("col1", axis=1)) # Not in place

# get column and index names
print(df.columns)
print(df.index)

# Sort/order a df
print(df.sort_values("col2"))

# find null vals
print(df.isnull())

# Pivot table (Turn A and B into index, C into columns, and D is the data)
data = {"A":["foo", "foo", "foo", "bar", "bar", "bar"],
        "B":["one", "one", "two", "two", "one", "one"],
        "C":["x", "y", "x", "y", "x", "y"],
        "D":[1, 3, 2, 5, 4, 1]}
df = pd.DataFrame(data)
print(df)
print(df.pivot_table(values="D", index=["A", "B"], columns="C"))

