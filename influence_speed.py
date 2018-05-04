import glob
import json
import networkx as nx
import matplotlib.pyplot as plt

THREADHOLD = 0.5
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
                    G.add_edge(current_node,line)
                    print("add the edge")
                except:
                    print("add  node mai dai")
    except:
        print("read file mai dai")

def influence(all_influence, active, in_active):
    # print(all_influence)
    relate = []
    for active_node in active:
        for node in G.neighbors(active_node):
            in_active[node] += 1
            relate.append(node)
    relate = list(set(relate) - set(all_influence))
    active = []
    for node in relate:
        if in_active[node] / G.in_degree(node) >= THREADHOLD:
            active.append(node)
    if active != []:
        for node in active:
            all_influence.append(node)
        influence(all_influence, active, in_active)

temp_in_active = {}
for node in list(G.node):
    temp_in_active[node] = 0

S = []
not_S = list(G.node()) + []
for i in range(10):
    max = -1
    max_node = 0
    count = 0
    for not_node in not_S:
        print(count, S)
        count+=1
        all_influence = S + [not_node]
        active = all_influence + []
        in_active = temp_in_active.copy()
        influence(all_influence, active, in_active)
        number_of_influence = len(all_influence)
        if number_of_influence > max:
            # print(number_of_influence)
            max = number_of_influence
            max_node = not_node
    if max_node != 0:
        S.append(max_node)
        not_S.remove(max_node)
    print(S)

    