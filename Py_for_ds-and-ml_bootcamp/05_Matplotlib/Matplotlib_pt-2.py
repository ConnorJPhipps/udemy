# Examples from section 7 of the Python for DS and ML Bootcamp on Udemy
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

# Creating subplots
'''
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].plot(x, y)
ax[0].set_title("Title 1")
ax[1].plot(y, x)
plt.show()
'''
'''
fig, ax = plt.subplots(nrows=1, ncols=2)
for axes in ax:
    axes.plot(x, y)
plt.show()
'''

# Figure Size and DPI
# Figsize is width and height in inches
# DPI is pixels per inch
'''
fig = plt.figure(figsize=(3, 2), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)
plt.show()
'''
'''
fig = plt.figure(figsize=(8, 2), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)
plt.show()
'''
'''
fig, ax = plt.subplots(2, 1, figsize=(8, 2))
ax[0].plot(x, y)
ax[1].plot(y, x)
plt.tight_layout()
plt.show()
'''

# Save a figure (many common formats)
'''
fig, ax = plt.subplots(2, 1, figsize=(8, 2))
ax[0].plot(x, y)
ax[1].plot(y, x)
plt.tight_layout()
fig.savefig("Matplotlib_example-output/Matplotlib_pt-2.png")
'''

# Legend

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, x**2, label="X Squared")
ax.plot(x, x**3, label="X Cubed")
ax.legend(loc="lower right")
plt.tight_layout()
plt.show()
