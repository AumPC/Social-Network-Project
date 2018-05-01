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
head_node = []
RULE = 0.5
S = []

for file in glob.glob('data/clean_follower/*'):
    current_node = file.strip('.txt').split('\\')[1]
    head_node.append(current_node)

not_S = head_node
count = 0

while(S != not_S):
    max = 0
    count = 0
    in_active = {}
    for node in mahidolU_follower:
        in_active[node] = 0
    for not_node in not_S:
        new_S = S + [not_node]
        for node_S in new_S:
            file = 'data/clean_follower/' + str(node_S) + '.txt'
            with open(file) as f:
                for follower in f:
                    follower = follower.rstrip('\n')
                    in_active[follower] = in_active[follower] + 1 
        for node in not_S:
            if out_degree[node] != 0:        
                if (in_active[node] / out_degree[node]) >= RULE:
                    count+=1
        if count >= max:
            new_node = node_S
        print(S)
    S.append(new_node)
    not_S.remove(new_node)

print(S)
print(len(S))
