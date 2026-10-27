import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import psutil

import random
import time
import sys
from collections import deque, defaultdict

def measure_performance(search_algorithm, graph, start, end):
    start_time = time.time()
    path = search_algorithm(graph, start, end)
    end_time = time.time()
    
    # Measure memory usage
    memory_usage = sys.getsizeof(graph) + sum(sys.getsizeof(neighbors) for neighbors in graph.values())

    return path, end_time - start_time, memory_usage

def create_random_graph(num_nodes, num_edges):
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    
    # Randomly add edges
    while G.number_of_edges() < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v:  # Avoid self-loops
            G.add_edge(u, v)
    
    return G

def draw_graph(G, title):
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=15, font_weight='bold')
    plt.title(title)
    plt.show()

def bfs(G, start, end):
    start_time = time.time()
    visited = set()
    queue = [(start, [start])]

    while queue:
        current_node, path = queue.pop(0)
        if current_node == end:
            time_taken = time.time() - start_time
            memory_usage = psutil.Process().memory_info().rss / (1024 * 1024)  # in MB
            return path, time_taken, memory_usage
        
        if current_node not in visited:
            visited.add(current_node)
            neighbors = G.neighbors(current_node)
            for neighbor in neighbors:
                queue.append((neighbor, path + [neighbor]))
    
    return None, None, None

def dfs(G, start, end):
    start_time = time.time()
    visited = set()
    
    def _dfs(current_node, path):
        if current_node == end:
            time_taken = time.time() - start_time
            memory_usage = psutil.Process().memory_info().rss / (1024 * 1024)  # in MB
            return path, time_taken, memory_usage
        
        visited.add(current_node)
        for neighbor in G.neighbors(current_node):
            if neighbor not in visited:
                result = _dfs(neighbor, path + [neighbor])
                if result:
                    return result
        return None

    return _dfs(start, [start])

# Parameters
num_nodes = 10
num_edges = 15  # Adjust as needed for connectivity

V=10
E=15
# Create and draw the random graph
random_graph = create_random_graph(num_nodes, num_edges)
draw_graph(random_graph, "Random Graph with 10 Nodes")

# Find paths using BFS and DFS
start_node = random.randint(0, num_nodes - 1)
end_node = random.randint(0, num_nodes - 1)

while start_node == end_node:  # Ensure start and end are different
    end_node = random.randint(0, num_nodes - 1)

bfs_path, bfs_time, bfs_memory = bfs(random_graph, start_node, end_node)
dfs_path, dfs_time, dfs_memory = dfs(random_graph, start_node, end_node)
print("\n\t======== BFS and DFS Algorithms ========\n")
# Print results
print(f"\tBFS: Shortest path from node {start_node} to node {end_node}:\n\t {bfs_path}\n\t Time Taken: {bfs_time:.6f}s\n\t Memory Usage: {bfs_memory:.2f} MB""\n\t Time Complexity: O(V + E)""\n\t Time Complexity: O(10 + 15)\n")
print(f"\tDFS: Shortest path from node {start_node} to node {end_node}:\n\t {dfs_path}\n\t Time Taken: {dfs_time:.6f}s\n\t Memory Usage: {dfs_memory:.2f} MB""\n\t Time Complexity: O(V + E)""\n\t Time Complexity: O(10 + 15)\n")

