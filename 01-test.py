#%%
import networkx as nx
import matplotlib.pyplot as plt

#%%
G = nx.Graph()

#%%
G.add_node(1)
G.add_nodes_from([2,3])

#%%
# this part adds a path graph H as a whole to graph G
# H is represented as a single node in G
H = nx.path_graph(10)
G.add_node(H)

#%%
#add nodes from 
# this will iterate H and add nodes from H
G.add_nodes_from(H)
#%%
nx.draw(G)
#plt.show()

# %%
print(G)


# %%
# edges 
G.add_edge(1,2)

# %%
e=(2,3)
G.add_edge(*e) # unpack the edge tuple

# %%
list_of_edges = [(3,4), (3,2)]
G.add_edges_from(list_of_edges)
#%%
nx.draw(G)

# %%
G.add_edges_from(H.edges())

# %%
nx.draw(G)

# %%
print( f"{G.nodes()}, {G.edges()}, {G.neighbors(1)}")

# %%
