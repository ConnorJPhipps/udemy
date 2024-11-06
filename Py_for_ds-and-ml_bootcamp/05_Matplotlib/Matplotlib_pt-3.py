# Examples from section 7 of the Python for DS and ML Bootcamp on Udemy
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

# Change line color
'''
fig = plt.figure()
ax= fig.add_axes([0, 0, 1, 1])
#ax.plot(x,y, color="green") # By color name
ax.plot(x,y, color="#FF8C00") # By color hexcode 
plt.show()
'''

# Change line width
'''
fig = plt.figure()
ax= fig.add_axes([0, 0, 1, 1])
ax.plot(x,y, linewidth=10)
plt.show()
'''

# Change line transparency
'''
fig = plt.figure()
ax= fig.add_axes([0, 0, 1, 1])
ax.plot(x,y, alpha=0.5)
plt.show()
'''

# Line styles
'''
fig = plt.figure()
ax= fig.add_axes([0, 0, 1, 1])
ax.plot(x,y, linestyle=":")
plt.show()
'''

# Working with markers
'''
fig, ax = plt.subplots()
ax.plot(x,y, marker="o", markersize=20,
        markerfacecolor='yellow', markeredgewidth=3)
plt.show()
'''

# Y and X limits
fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlim([0, 1]) # With its own set function
ax.set(ylim=[0,5]) # With the general ax set function
plt.show()

# A few different ways to work with fig, axis objects
'''
fig, ax = plt.subplots()
ax.plot(x,y, linestyle=":")
plt.show()
'''
'''
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax2.plot(y, x)
plt.show()
'''
'''
fig, ax = plt.subplots(1, 2, sharey=True)
ax[0].plot(x, y)
ax[1].plot(y, x)
plt.show()
'''