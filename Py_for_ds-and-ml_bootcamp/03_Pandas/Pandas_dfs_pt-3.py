# Examples from section 6 of the Python for DS and ML Bootcamp on Udemy
import numpy as np
import pandas as pd
from numpy.random import randn

outside = ["G1", "G1", "G1", "G2", "G2", "G2"]
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

# This generates a df with multiple indices (similar to group by if you don't reset index)
df = pd.DataFrame(randn(6,2), hier_index, ["A","B"])
print(df)

# Using multiindex
print(df.loc["G1"])
print(df.loc["G1"].loc[1])

# Naming indices (for readability)
df.index.names = ["Groups", "Num"]
print(df)

# Cross-section (similar to regular access but can skip groups
print(df.xs("G1"))
print(df.xs(1, level="Num"))