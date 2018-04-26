import glob
import networkx as nx

def get_graph(data_path):

    G = nx.Graph()

    for file in glob.glob(data_path):

        # for window environment
        # current_node = file.strip('.txt').split('\\')[-1]

        # for ubuntu environment
        current_node = file.strip('.txt').split('/')[-1]

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

    return G
