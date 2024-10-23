# # NumPy Exercises
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[1]:

import numpy as np



# #### Create an array of 10 zeros 

# In[2]:


print(np.zeros(10))


# #### Create an array of 10 ones

# In[3]:

print(np.ones(10))



# #### Create an array of 10 fives

# In[4]:

tmp = np.zeros(10)
tmp[:] = 5
print(tmp)



# #### Create an array of the integers from 10 to 50

# In[5]:

print(np.arange(10,51))



# #### Create an array of all the even integers from 10 to 50

# In[6]:
print(np.arange(10,51,2))




# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[7]:
tmp = np.arange(0,9)
tmp = tmp.reshape(3,3)
print(tmp)




# #### Create a 3x3 identity matrix

# In[8]:
print(np.eye(3))




# #### Use NumPy to generate a random number between 0 and 1

# In[15]:
print(np.random.rand(1))




# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[33]:
print(np.random.randn(25))



# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[36]:
print(np.linspace(0,1,20))




# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[38]:


mat = np.arange(1,26).reshape(5,5)
mat
print(mat)



# ### Now do the following

# #### Get the sum of all the values in mat

# In[50]:
print(mat.sum())




# #### Get the standard deviation of the values in mat

# In[51]:
print(mat.std())




# #### Get the sum of all the columns in mat

# In[53]:
print(mat.sum(axis=0))




# # Great Job!
