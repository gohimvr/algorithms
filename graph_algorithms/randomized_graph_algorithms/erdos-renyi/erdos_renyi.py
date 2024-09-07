import random
import networkx as nx

'''
Simple implementation of Erdős–Rényi algorithm for randomly generating graphs, specifically the model
G(n,p) model, taking n nodes connected randomly with p probability.

Runtime: O(n^2)
'''


def erdos_renyi(n: int, p: float) -> nx.Graph:
    g = nx.Graph()
    g.add_nodes_from(range(n))
    for i in g.nodes:
        for j in g.nodes:
            if i != j:
                r = random.random()
                if r <= p:
                    g.add_edge(i, j)
    return g





