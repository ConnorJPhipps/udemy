import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

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

# Get popular movies
pop_movies = ratings[ratings["num_ratings"] > 50].index
df = df[df["title"].isin(pop_movies)]

# Get matrix of movie reviews by user
movie_mat = df.pivot_table(index="user_id", columns="title", values="rating")

# Generate ccmat of movie reviews
cc_mat = movie_mat.corr()

# Zero out bottom half and diagonal of ccmat
cc_mat = cc_mat.where(np.triu(np.ones(cc_mat.shape).astype(bool),1))

# Fix index name to avoid later conflicts
cc_mat.index.name = "title_1"

# Convert ccmat to edges
network_edges = cc_mat.stack().reset_index()
network_edges = network_edges.rename(columns={"title": "title_2", 0: "corr"})

# Remove weaker connections
network_edges = network_edges[(network_edges["corr"] > .5) | (network_edges["corr"] < -.5)]
network_edges.reset_index()

#sns.displot(network_edges["corr"])
#plt.show()

movie_net = nx.from_pandas_edgelist(network_edges, source="title_1", target="title_2", edge_attr="corr")

# Generate modularity communities
communities = nx.community.greedy_modularity_communities(movie_net, weight="corr")
#print(len(communities))


# Get pos for clusters and scale the graph
super_graph = nx.cycle_graph(len(communities))
super_pos = nx.spring_layout(movie_net, k=100, scale=500, seed=429)

# Use supernode to center each cluster
centers = list(super_pos.values())
pos = {}
for center, comm in zip(centers, communities):
    pos.update(nx.spring_layout(nx.subgraph(movie_net, comm), center=center), seed=1430)

nx.draw_networkx_edges(movie_net, pos=pos)

plt.tight_layout()
plt.show()


'''
# Color nodes by cluster
for nodes, clr in zip(communities)
'''

'''
#upper_triangle_booleans = np.triu(np.ones(cc_mat.shape).astype(np.bool),1)
cc_mat_np = pd.DataFrame.to_numpy(cc_mat)
cc_mat_np = np.triu(cc_mat_np, 1)
print(cc_mat_np.shape)
#np.fill_diagonal(cc_mat_np, 0)
#print(cc_mat_np)
cc_mat_np = np.triu(cc_mat_np, 1)
print(cc_mat_np.shape)
'''