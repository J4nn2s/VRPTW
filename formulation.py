from pulp import *
import json
import networkx as nx

with open("vrptw_graph.json", "r") as f:
    data = json.load(f)
G = nx.Graph()

G = nx.node_link_graph(data)




