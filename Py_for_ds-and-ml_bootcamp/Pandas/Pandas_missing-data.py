# Examples from section 6 of the Python for DS and ML Bootcamp on Udemy
import numpy as np
import pandas as pd

d = {"A": [1, 2, np.nan], "B": [5, np.nan, np.nan], "C": [1, 2, 3]}
df = pd.DataFrame(d)
print(df)

# Remove all rows with any na values
print(df.dropna())

# To remove all columns with na change the axis value
print(df.dropna(axis=1))

# Use a threshold for dropping na values (how many nas to drop)
print(df.dropna(thresh=2))

# Filling na values with new values
print(df.fillna(value="Fill"))
print(df["A"].fillna(value=df["A"].mean()))