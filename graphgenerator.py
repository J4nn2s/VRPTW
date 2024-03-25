import networkx as nx
import random

def generate_vrptw_graph(num_customers, num_vehicles, vehicle_capacity, time_window_range, service_duration_range, distance_range):
    G = nx.Graph()
    
    # Add depot
    G.add_node(0, demand=0, time_window=(0, float('inf')), service_duration=0)
    
    # Add customers
    for i in range(1, num_customers+1):
        demand = random.randint(1, 10)  # Random demand for the customer
        time_window_start = random.randint(0, 50)
        time_window_end = random.randint(time_window_start, 100)
        service_duration = random.randint(1, 5)
        G.add_node(i, demand=demand, time_window=(time_window_start, time_window_end), service_duration=service_duration)
    
    # Add edges with random distances
    for i in range(num_customers+1):
        for j in range(i+1, num_customers+1):
            distance = random.uniform(distance_range[0], distance_range[1])
            G.add_edge(i, j, distance=distance)
    
    return G

num_customers = 5
num_vehicles = 2
vehicle_capacity = 20
time_window_range = (0, 100)
service_duration_range = (1, 5)
distance_range = (1, 10)

G = generate_vrptw_graph(num_customers, num_vehicles, vehicle_capacity, time_window_range, service_duration_range, distance_range)

# Print nodes and their attributes
print("Nodes:")
for node in G.nodes(data=True):
    print(node)

# Print edges and their attributes
print("\nEdges:")
for edge in G.edges(data=True):
    print(edge)
