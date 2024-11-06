# Examples from section 8 of the Python for DS and ML Bootcamp on Udemy
import seaborn as sns
import matplotlib.pyplot as plt


# Load a dataframe from seaborn called "tips"
tips = sns.load_dataset("tips")

# Dist plot with KDE and 30 distinct bins for data
'''
sns.displot(tips["total_bill"], kde=True, bins=30)
plt.show()
'''

# 2 distributions for bivariate data
'''
sns.jointplot(x="total_bill", y="tip", data=tips)
plt.show()
'''

'''
sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
plt.show()
'''

# Bivariate plot with a regression line
'''
sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
plt.show()
'''

# Pairwise relationship (diagonal is histogram of distribution)
'''
sns.pairplot(tips)
plt.show()
'''

'''
sns.pairplot(tips, hue="sex")
plt.show()
'''

# Rugplots (makes a dash at each unique location like a histogram without a y component)
sns.rugplot(tips["total_bill"])
plt.show()
