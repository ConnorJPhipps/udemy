# Examples from section 5 of the Python for DS and ML Bootcamp on Udemy
import numpy as np
import pandas as pd
# 03_Pandas is built off of numpy

labels = ["a", "b", "c"]
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {"a": 10, "b": 20, "c": 30}

# Different ways to make a pandas series
print(pd.Series(data=my_data))
print(pd.Series(data=my_data, index=labels))
print(pd.Series(arr))
print(pd.Series(arr,labels))
print(pd.Series(d))

# Panda's series can hold many different data types
print(pd.Series(data=labels))
print(pd.Series(data=[sum, print, len]))

# Panda's uses index to look up information
ser1 = pd.Series([1, 2, 3, 4], ["USA", "Germany", "France", "Spain"])
ser2 = pd.Series([1, 2, 5, 4], ["USA", "Germany", "Italy", "Spain"])
print(ser1["USA"])
ser3 = pd.Series(data=labels)
print(ser3[0])

# Working with Series
print(ser1 + ser2)