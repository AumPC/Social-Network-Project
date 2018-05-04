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

# G = nx.DiGraph()
# G.add_edge(1,2)
# G.add_edge(1,9)
# G.add_edge(8,3)
# G.add_edge(2,7)
# G.add_edge(6,3)
# G.add_edge(7,4)
# G.add_edge(7,5)
# G.add_edge(7,6)

out_degree = G.out_degree()
in_degree = G.in_degree()

print(out_degree)

f = open("in-degree.txt",'a')
# f.write(str)

# RULE = 0.5
# S = []
# not_S = list(G.node())
# count = 0
# active = []
# best_node = 0

# print(not_S)

# for i in range(4):
#     # print('i', i)
#     best_node = 0
#     active = S + []
#     max = -1
#     count = 0
#     for not_node in not_S:
#         count+=1
#         # print('not_node', not_node)
#         if not_node not in active:
#             active.append(not_node)
#         up = 1
#         not_active = list(set(list(G.node())) - set(active))
#         while(up):
#             fact = 0
#             for node in not_active:
#                 # print('node', node)
#                 all_neighbors = list(G.neighbors(node))
#                 active_neighbors = list(set(list(all_neighbors)) & set(active))
#                 if len(all_neighbors) != 0:
#                     if len(active_neighbors) / len(all_neighbors) >= RULE:
#                         if node not in active:
#                             active.append(node)
#                         # count+=1
#                         # print(count)
#                         fact = 1
#                 # print("all_neighbors",all_neighbors)
#                 # print("active_neighbors", active_neighbors)
#                 # print("active", active)
#                 # input()
#             not_active = list(set(list(G.node())) - set(active))
#             if fact == 0:
#                 up = 0
#         if len(active) > max:
#             max = len(active)
#             best_node = not_node
#         active = S + []
#         # print("best_node", best_node) 
#         print("S", S ,'count', count)
#         # print("not_S", not_S)
#         # print("not_node", not_node)
#         # print("active", active)
#         # print()
#     S.append(best_node)
#     not_S = list(set(list(G.node())) - set(S))
# print(S)