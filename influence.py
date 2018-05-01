import glob
import json
import networkx as nx
import matplotlib.pyplot as plt


mahidolU_follower = []
G = nx.DiGraph()

with  open("data/mahidolU.txt") as f:
    for line in f:
        mahidolU_follower.append(line.rstrip('\n'))

for file in glob.glob('data/clean_follower/*'):
    current_node = file.strip('.txt').split('\\')[1]
    if current_node not in G:
        G.add_node(current_node)
    try:
        with open(file) as f:
            for line in f:
                line = line.rstrip('\n')
                try:
                    G.add_edge(line,current_node)
                    print("add the edge")
                except:
                    print("add  node mai dai")
    except:
        print("read file mai dai")

out_degree = G.out_degree()
RULE = 0.5
S = []
not_S = list(G.node())
count = 0
active = []
best_node = 0

for i in range(10):
    best_node = 0
    active = S
    max = 0
    for not_node in not_S:
        active.append(not_node)
        up = 1
        while(up):
            fact = 0
            for node in list(G.node()):
                all_neighbors = list(G.neighbors(node))
                active_neighbors = list(set(list(all_neighbors)) & set(active))
                if len(all_neighbors) != 0:
                    if len(active_neighbors) / len(all_neighbors) >= RULE:
                        active.append(node)
                        fact = 1
            if fact == 0:
                up = 0
        if len(active) > max:
            max = len(active)
            best_node = not_node
        active = S
        print(S)
    S.append(best_node)
