#genereate a random charecter to find short path and apply BFS and DFS algorithm
import random
import time
import sys
from collections import deque, defaultdict

def generate_random_graph(num_vertices, num_edges):
    """
    CS student algorithm course 
    Generates a random undirected graph with random character vertices.
    Parameters:
    - num_vertices: The number of vertices in the graph.
    - num_edges: The number of edges in the graph.
    
    Returns:
    - A dictionary representing the adjacency list of the graph.
    """
    graph = defaultdict(list)
    # Generate characters A, B, C, ..., Z, AA, AB, ..., etc. for up to 100 nodes
    vertices = [chr(i) for i in range(65, 65 + min(num_vertices, 26))]  # A-Z
    if num_vertices > 26:
        vertices += [f"{chr(65 + (i // 26))}{chr(65 + (i % 26))}" for i in range(26, num_vertices)]

    # Ensure the number of edges does not exceed the maximum possible in an undirected graph
    max_edges = num_vertices * (num_vertices - 1) // 2
    num_edges = min(num_edges, max_edges)

    # Create a set to track edges to avoid duplicates
    edges = set()

    while len(edges) < num_edges:
        u, v = random.sample(vertices, 2)  # Ensure u and v are different
        if (u, v) not in edges and (v, u) not in edges:
            edges.add((u, v))
            graph[u].append(v)
            graph[v].append(u)  # Undirected graph

    return dict(graph), vertices

def draw_graph(graph):
    """
    Draws the graph in a simple text format.
    
    Parameters:
    - graph: The adjacency list of the graph.
    """
    print("Text Drawing of the Graph (all nodes):")
    
    if not graph:
        print("Empty graph.")
        return
    
    # Print all nodes and their connections
    for node in graph.keys():
        neighbors_str = ', '.join(graph[node])
        print(f"{node}: {neighbors_str}")

def bfs_shortest_path(graph, start, end):
    """
    Perform BFS to find the shortest path in an unweighted graph.
    
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    """
    queue = deque([start])
    visited = {start: None}  # Track visited nodes and their parents

    while queue:
        current = queue.popleft()
        
        if current == end:
            # Reconstruct the path
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1]  # Return reversed path

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)
    
    return None  # Return None if there is no path

def dfs_shortest_path(graph, start, end):
    """
    Perform DFS to find the shortest path in an unweighted graph.
    
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    """
    stack = [start]
    visited = {start: None}  # Track visited nodes and their parents

    while stack:
        current = stack.pop()
        
        if current == end:
            # Reconstruct the path
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1]  # Return reversed path

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited[neighbor] = current
                stack.append(neighbor)
    
    return None  # Return None if there is no path

# Measuring runtime and memory usage
def measure_performance(search_algorithm, graph, start, end):
    # Measure time
    start_time = time.time()
    path = search_algorithm(graph, start, end)
    end_time = time.time()
    
    # Measure memory usage
    memory_usage = sys.getsizeof(graph) + sum(sys.getsizeof(node) for node in graph)

    return path, end_time - start_time, memory_usage

# Function to calculate number of vertices (V) and edges (E)
def calculate_vertices_and_edges(graph):
    V = len(graph)
    E = sum(len(neighbors) for neighbors in graph.values()) // 2  # Each edge is counted twice
    return V, E

# Main execution
num_vertices = 100  # Set to 100 nodes
num_edges = 300  # Adjust this number based on your requirements
random_graph, vertices = generate_random_graph(num_vertices, num_edges)

# Print the entire generated graph (all nodes)
draw_graph(random_graph)

print("\n=======  BFS and DFS Algorithms  =======\n")

# Calculate V and E for the generated graph
V, E = calculate_vertices_and_edges(random_graph)

# BFS on the random graph
start_node = random.choice(vertices)
end_node = random.choice(vertices)

print(f"\tStart Node: {start_node}, End Node: {end_node}")

path_bfs, time_bfs, memory_bfs = measure_performance(bfs_shortest_path, random_graph, start_node, end_node)
print(f"\t\n -----------------")
print(f"\t\nBFS Shortest path from {start_node} to {end_node}:\n")
print(f"\tPath: {path_bfs}")
print(f"\tTime taken: {time_bfs:.6f} seconds")
print(f"\tMemory usage: {memory_bfs} bytes")
print(f"\tTime Complexity: O(V + E)")
print(f"\tTime Complexity: O({V} + {E})")

# DFS on the random graph
path_dfs, time_dfs, memory_dfs = measure_performance(dfs_shortest_path, random_graph, start_node, end_node)
print(f"\t\n -----------------")
print(f"\t\nDFS Shortest path from {start_node} to {end_node}:\n")
print(f"\tPath: {path_dfs}")
print(f"\tTime taken: {time_dfs:.6f} seconds")
print(f"\tMemory usage: {memory_dfs} bytes")
print(f"\tTime Complexity: O(V + E)")
print(f"\tTime Complexity: O({V} + {E})\n")