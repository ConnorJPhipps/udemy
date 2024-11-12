import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Load tips dataset from seaborn
tips = sns.load_dataset("tips")

# Set to default seaborn theme
sns.set_theme()

# Bar plot
'''
sns.barplot(x="sex", y="total_bill", data=tips)
plt.show()
'''

# Bar plot with a different estimator (function to estimate in each categorical bin like mean, sd, ...)
'''
sns.barplot(x="sex", y="total_bill", data=tips, estimator=np.std)
plt.show()
'''

# Count plot (bar plot but estimator is number of occurrences)
'''
sns.countplot(x="sex", data=tips)
plt.show()
'''

# Box plots
'''
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()
'''

# Box with hue
'''
sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips)
plt.show()
'''

# Violin plot
'''
sns.violinplot(x="day", y="total_bill", hue="day", data=tips)
plt.show()
'''

# Violin with split
'''
sns.violinplot(x="day", y="total_bill", hue="sex", split=True, data=tips)
plt.show()
'''

# Strip plot (default is with jitter here)
'''
sns.stripplot(x="day", y="total_bill", data=tips)
plt.show()
'''

