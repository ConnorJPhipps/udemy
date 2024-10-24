# Examples from section 6 of the Python for DS and ML Bootcamp on Udemy
import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
print(df)

# Conditional selection
print( df > 0)
booldf = df > 0
print(df[booldf])
# of
print(df[df > 0])

# Use series to find rows meeting condition (no  NaN, only True rows)
print(df["W"] > 0)
print(df[df["W"] > 0])

# eg 2
print(df[df["Z"] < 0])

# The returned data is a df
resultdf = df[df["W"] > 0]
print(resultdf["X"])
# or
print(df[df["W"]>0]["X"])

# With multiple cols
print(df[df["W"]>0][["Y", "X"]])

# Multiple conditions (& for and; | for or)
print(df[(df["W"] > 0) | (df["Y"] > 1)])

# Change df index or reset index (not inplace by default)
print(df.reset_index())

newind = "CA NY WY OR CO".split()
df['States'] = newind
print(df)
print(df.set_index("States")) # not in place