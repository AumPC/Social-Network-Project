import networkx as nx
import community
import matplotlib.pyplot as plt
import graph_generater

# G = nx.random_graphs.powerlaw_cluster_graph(300, 1, .4)
G = graph_generater.get_graph('data/clean_follower/*')

part = community.best_partition(G)
values = []
for node in G.nodes():
    values.append(part.get(node))

nx.draw_spring(G, cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
plt.show(G)
