# Examples from section 5 of the Python for DS and ML Bootcamp on Udemy
import numpy as np

# Vectors are 1-D arrays
my_list = [1,2,3]
my_np_arr = np.array(my_list)
print(my_list)
print(my_np_arr)
# Matrices are 1 or more dimensions arrays
my_matrix = [[1,2,3], [4,5,6], [7,8,9]]
my_np_matrix = np.array(my_matrix)
print(my_np_matrix)

# Np matrices can also be made in a way similar to range in python
print(np.arange(0,10))

# For an np matrix of 0s (for ex to make an empty array of a known shape
print(np.zeros((2,3)))
# Can also get 1s with np.ones

# Np linspace will make an array between the provided range with a provided number of points
# Eg for 10 points between 10 and 15
print(np.linspace(10,15,10))

# Identity matrices can be made with np.eye (all zeros but 1s on the diagonal)
print(np.eye(4))

# To gen arrays of random numbers there are quite a few options
# 1-d array of numbers from a random dist between 0 and 1
np.random.rand(5)
# 2-d array of numbers from a random dist between 0 and 1
np.random.rand(5,5)
# Gaussian dis for random (normal dist centered around 0)
np.random.randn(5,2)
# For random ints (args are: Low, high, size)
np.random.randint(1,51,50)

# Array attributes
arr = np.arange(25)
print(arr)

ranarr = np.random.randint(0,50,10)
print(ranarr)

# Reshape array (must be same number of elements)
print(arr.reshape(5,5))

# Find max/min value and index
print(ranarr.max())
print(ranarr.min())
print(ranarr.argmax())
print(ranarr.argmin())

# Get sape of vector or matrix
print(arr.shape)
tmp = arr.reshape(5,5)
print(tmp.shape)

# Get datatype
print(arr.dtype)

