# -*- coding: utf-8 -*-
"""
Created on Wed May  2 00:50:11 2018

@author: sarac
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:36:10 2018

visualize full-graph with networkx & vispy 
"""

import glob
import json
import networkx as nx

mahidolU_follower = []
in_degree = {}
out_degree = {}
G = nx.DiGraph()

count = 0

with  open("data/mahidolU.txt") as f:
    for line in f:
        mahidolU_follower.append(line.rstrip('\n'))
    
for id in mahidolU_follower:
    in_degree[id] = 0
    out_degree[id] = 0 

for file in glob.glob('data/clean_follower/*'):
    current_node = file.strip('.txt').split('\\')[1]
    if current_node not in G:
        G.add_node(current_node)
    try:
        with open(file) as f:

            for line in f:
                line = line.rstrip('\n')
                out_degree[current_node]+=1
                in_degree[line]+=1
                try:
                    G.add_edge(line,current_node)
                    print("add the edge")
                    count+=1

                except:
                    print("add  node mai dai")
            
    except:
        print("read file mai dai")
            
solo = 0
for id in in_degree:
    if in_degree[id] == 0 and out_degree[id] == 1:
        print(id)
        solo+=1
        
print(solo)
print(count)

"""
Vispy plot 
"""

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