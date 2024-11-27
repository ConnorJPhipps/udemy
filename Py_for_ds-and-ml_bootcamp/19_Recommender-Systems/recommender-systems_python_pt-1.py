import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Get user data
column_names = ["user_id", "item_id", "rating", "timestamp"]
df = pd.read_csv("u.data", sep="\t", names=column_names)
#print(df.head())

# Get movie id and title data
movie_titles = pd.read_csv("Movie_Id_Titles")
#print(movie_titles.head())

# Merge dfs
df = pd.merge(df, movie_titles, on="item_id")
#print(df.head())

# Look at the average ratings of movies by title (but this does not account for how many ratings there were
#print(df.groupby("title")["rating"].mean().sort_values(ascending=False).head())

# Here we actually look at the number of ratings
#print(df.groupby("title")["rating"].count().sort_values(ascending=False).head())

# Let's add this data to a df
ratings = pd.DataFrame(df.groupby("title")["rating"].mean())
ratings["num_ratings"] = df.groupby("title")["rating"].count()
print(ratings.head())

# Plot the number of ratings (most movies have under 100 ratings)
#sns.histplot(ratings["num_ratings"])
#plt.show()

# Rating bins are largest at whole numbers with most movies being around 3
#sns.histplot(ratings["rating"])
#plt.show()

# Look at how these factors are associated
#sns.jointplot(x="rating", y="num_ratings", data=ratings, alpha=0.5)
#plt.show()