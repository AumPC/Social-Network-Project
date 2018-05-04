import glob
import json
import networkx as nx
import matplotlib.pyplot as plt


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
    if in_degree[id] == 0 and out_degree[id] == 0:
        print(id)
        solo+=1
print(solo)
print(count)
x = nx.in_degree_centrality(G)
# print(x)
for key, value in sorted(x.items(), key=lambda item: (item[1], item[0])):
    print (str(key) + "," + str(value))

# def get_value(item):
#     return item[1]
# sorted_in_degree = sorted(G.in_degree(), key=get_value, reverse=True)
# # print(sorted_in_degree)
# sorted_out_degree = sorted(G.out_degree(), key=get_value, reverse=True)
# # print(sorted_out_degree)
# # a = nx.in_degree_centrality(G)
# # print(a)
# # sorted_in_centrality = sorted(nx.in_degree_centrality(G), key=get_value, reverse=True)
# # print(sorted_in_centrality)

# # f = open('data/in_degree_centrality.txt', 'a')
# # for i in sorted_in_centrality:
# #     f.write(str(i[0]) + "," + str(i[1]) + "\n")
# # f.close()

# f = open('data/in_degree.txt', 'a')
# for i in sorted_in_degree:
#     f.write(str(i[0]) + "," + str(i[1]) + "\n")
# f.close()

# f = open('data/out_degree.txt', 'a')
# for i in sorted_out_degree:
#     f.write(str(i[0]) + "," + str(i[1]) + "\n")
# f.close()


# # y = nx.out_degree_centrality(G);
# # for key, value in sorted(y.items(), key=lambda item: (item[1], item[0])):
# #     print (key, ":", value)

# # z = nx.degree_centrality(G);
# # for key, value in sorted(z.items(), key=lambda item: (item[1], item[0])):
# #     print (key, ":", value)

# #nx.draw(G,node_size = 20,width = 0.5, edge_color = "grey")
# #plt.show()
# #plt.savefig("Graph.png", format="PNG")
