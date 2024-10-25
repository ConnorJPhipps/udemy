# Examples from section 7 of the Python for DS and ML Bootcamp on Udemy
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

# Functional methods (not as good)
'''
plt.plot(x, y)
plt.show()

plt.plot(x, y)
plt.xlabel("X label")
plt.ylabel("Y label")
plt.title("Title")
plt.show()
'''
'''
# Multiple plots (with function)
plt.subplot(1, 2, 1)
plt.plot(x, y, "r")

plt.subplot(1, 2, 2)
plt.plot(y, x, "b")
plt.show()
'''
# Object method to make graphs
'''
fig = plt.figure() # Make figure object
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # Add axes to figure (Left, Bottom, Width, Height)
axes.plot(x, y)
axes.set_xlabel("X Label")
axes.set_ylabel("Y Label")
axes.set_title("Set Title")
plt.show()
'''

# Multiple figs
'''
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
ax1.plot(x, y)
ax2.plot(y, x)
plt.show()
'''

# Move secondary fig
'''
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.4, 0.15, 0.4, 0.3])
ax1.plot(x, y)
ax2.plot(y, x)
plt.show()
'''

