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


t = []
for i in range(37):
    t.append(0)
    
for i in values:
    t[i] += 1
    
#for i in range(37):
#    print(i , "," , t[i])
    
    
A = graph_generater.get_digraph('data/clean_follower/*')

for i in range(37):
    d = []
    for j in G.node():
        if(part.get(node) == i):
            d.append(node)
    F = A.subgraph(d)
    print(len(F.node()))
    c = nx.in_degree_centrality(F)
    print(i , "," , c)

nx.draw_spring(G, cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
plt.show(G)


import sys

import networkx as nx

from vispy import app, scene
from vispy.visuals.graphs import layouts
import vispy.io as io 

canvas = scene.SceneCanvas(title='Result', size=(1024, 1024),
                           bgcolor='white', show=True)
view = canvas.central_widget.add_view('panzoom')

graph = nx.adjacency_matrix(G)
layout = layouts.get_layout('force_directed', iterations=100)
print('success')
print('plotting data do not terminate program about 30 miniutes long')

visual = scene.visuals.Graph(
    graph, layout=layout, line_color='red',line_width=0.1, arrow_type="triangle_30",
    arrow_size=30, node_symbol="disc", node_size=15, 
    face_color="blue", border_width=0, animate=True, directed=True,
    parent=view.scene)
print('plot done')

@canvas.events.draw.connect
def on_draw(event):
    if not visual.animate_layout():
        canvas.update()

if __name__ == '__main__':
    if sys.flags.interactive != 1:
        app.run()