import networkx as nx

def build_reason_graph(concepts):
    G = nx.DiGraph()
    for concept in concepts:
        G.add_node(concept)
    return G