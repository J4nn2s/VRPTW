import networkx as nx
import random
import matplotlib.pyplot as plt
import typing
import json


def generateVRPTWGraph(arcs: int, timeWindowRange: tuple, distanceRange: tuple) -> nx.Graph:
    G = nx.Graph()
    G.add_node(0)
    # Add details
    for i in range(1, arcs):
        G.add_node(i)
    
    # Add edges with random distances and service durations
    for i in range(arcs+1):
        for j in range(i+1, arcs+1):
            distance = random.uniform(distanceRange[0], distanceRange[1])
            timeWindow = timeWindowRange
            G.add_edge(i, j, distance=distance, timeWindow=timeWindow)
    
    return G

if __name__ == "__main__":
    print("Lets GO")
    arcs = 5
    timeWindowRange = (0, 5)
    distanceRange = (1, 10)

    G = generateVRPTWGraph(arcs, timeWindowRange, distanceRange)

    save = input("Graph speichern ? ('y')")

    if save == "y":

        # Convert graph to JSON data
        json_data = nx.node_link_data(G)
        # Save JSON data to a file
        with open("vrptw_graph.json", "w") as f:
            json.dump(json_data, f)

        print("Graph saved successfully as vrptw_graph.json.")

    # Print nodes and their attributes
    print("Nodes:")
    for node in G.nodes():
        print(node)

    # Print edges and their attributes
    print("\nEdges:")
    for edge in G.edges(data=True):
        print(edge)

    pos = nx.spring_layout(G)  # Layout des Graphen festlegen (hier: Frühjahrs-Layout)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')  # Graph plotten
    edge_labels = nx.get_edge_attributes(G, 'distance')  # Kantengewichte erhalten
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Kantengewichte plotten
    plt.title('VRPTW Graph')  # Titel des Plots festlegen
    plt.show()  # Plot anzeigenq