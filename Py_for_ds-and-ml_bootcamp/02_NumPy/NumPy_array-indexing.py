# Examples from section 5 of the Python for DS and ML Bootcamp on Udemy

import numpy as np

# Gen sample array
arr = np.arange(0,11)
print(arr)

# Similar to indexing from a python list
print(arr[5])
print(arr[1:5])
print(arr[:6])
print(arr[5:])

# You can also broadcast values
arr[0:5] = 100
print(arr)
arr = np.arange(0,11)

# This is a pass by reference NOT by value
slice_of_arr = arr[0:6]
slice_of_arr[:] = 99
print(arr)
arr = np.arange(0,11)

# To copy arrays
arr_copy = arr.copy()
print(arr_copy)
arr_copy[:] = 100
print(arr_copy)
print(arr)

# 2-d
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)
print(arr_2d[0][0])
print(arr_2d[0,0])

# Grabbing sections of matrices
print(arr_2d[:2,1:])

# Conditional selection
print(arr[arr>5])
