# Examples from section 6 of the Python for DS and ML Bootcamp on Udemy
import numpy as np
import pandas as pd
from numpy.random import randn

# Group by allows you to group rows based off of one or more columns
# and perform an aggregate function (eg sum, mean, max, min, ...etc)

data = {"Company": ["GOOG", "GOOG", "MSFT", "MSFT", "FB", "FB"],
        "Person": ["Sam", "Charlie", "Amy", "Vanessa", "Carl", "Sarah"],
        "Sales": [200, 120, 340, 124, 243, 350]}
df = pd.DataFrame(data)
print(df)

print(df.groupby("Company"))
by_comp = df.groupby("Company")
print(by_comp.mean(numeric_only=True)) # Have to add numeric only in recent versions of pd
print(by_comp.std(numeric_only=True).loc["FB"])

# Groupby and describe (get descriptive statistics)
print(df.groupby("Company").describe())
print(df.groupby("Company").describe().transpose())