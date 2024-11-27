import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Get user data
column_names = ["user_id", "item_id", "rating", "timestamp"]
df = pd.read_csv("u.data", sep="\t", names=column_names)

# Get movie id and title data
movie_titles = pd.read_csv("Movie_Id_Titles")

# Merge dfs
df = pd.merge(df, movie_titles, on="item_id")

# Let's add this data to a df
ratings = pd.DataFrame(df.groupby("title")["rating"].mean())
ratings["num_ratings"] = df.groupby("title")["rating"].count()

# Create matrix of user reviews with user_id as one index and movie_id as the other with the data being the rating
movie_mat = df.pivot_table(index="user_id", columns="title", values="rating")

# There are alot of missing values as most viewers have not seen all the movies
#print(movie_mat.head())

# Let's grab some popular movies
starwars_user_ratings = movie_mat["Star Wars (1977)"]
liarliar_user_ratings = movie_mat["Liar Liar (1997)"]

# Lets look at how other movie ratings are correlated with star wars rating
similar_to_starwars = movie_mat.corrwith(starwars_user_ratings)
similar_to_liarliar = movie_mat.corrwith(liarliar_user_ratings)
#print(similar_to_starwars.head())

# Remove null and make a df
corr_starwars = pd.DataFrame(similar_to_starwars, columns=["correlation"])
corr_starwars.dropna(inplace=True)

# Some movies look perfectly correlated (these are likely movies that have only been seen by one person)
# Let's add a threshold for number of reviews
corr_starwars = corr_starwars.join(ratings["num_ratings"])
corr_starwars = corr_starwars[corr_starwars["num_ratings"]>100]
#print(corr_starwars[corr_starwars["num_ratings"]>100].sort_values("correlation", ascending=False))

corr_liarliar = pd.DataFrame(similar_to_liarliar, columns=["correlation"])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings["num_ratings"])
corr_liarliar = corr_liarliar[corr_liarliar["num_ratings"]>100]
