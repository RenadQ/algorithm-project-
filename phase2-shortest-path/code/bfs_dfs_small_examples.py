import time
import sys
from collections import deque

def bfs_shortest_path(graph, start, end):
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

# Function to create a sample graph for testing
def create_graph1():
    return {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

def create_graph2():
    return {
        '1': ['2', '3'],
        '2': ['1', '4'],
        '3': ['1'],
        '4': ['2', '5', '6'],
        '5': ['4'],
        '6': ['4']
    }

# Measuring runtime and memory usage
def measure_performance(search_algorithm, graph, start, end):
    # Measure time
    start_time = time.time()
    path = search_algorithm(graph, start, end)
    end_time = time.time()

    # Measure memory usage
    memory_usage = sys.getsizeof(graph) + sum(sys.getsizeof(node) for node in graph)

    return path, end_time - start_time, memory_usage

# Main execution
print("=== BFS and DFS Algorithms ===\n")

# Test on Graph 1 (Example One) using BFS
graph1 = create_graph1()
path1_bfs, time1_bfs, memory1_bfs = measure_performance(bfs_shortest_path, graph1, 'A', 'F')
print("Example One: Graph 1 - BFS Shortest path from A to F:")
print(f"Path: {path1_bfs}")
print(f"Time taken: {time1_bfs:.6f} seconds")
print(f"Memory usage: {memory1_bfs} bytes\n")

# Test on Graph 1 (Example One) using DFS
path1_dfs, time1_dfs, memory1_dfs = measure_performance(dfs_shortest_path, graph1, 'A', 'F')
print("Example One: Graph 1 - DFS Shortest path from A to F:")
print(f"Path: {path1_dfs}")
print(f"Time taken: {time1_dfs:.6f} seconds")
print(f"Memory usage: {memory1_dfs} bytes\n")

# Test on Graph 2 (Example Two) using BFS
graph2 = create_graph2()
path2_bfs, time2_bfs, memory2_bfs = measure_performance(bfs_shortest_path, graph2, '1', '5')
print("Example Two: Graph 2 - BFS Shortest path from 1 to 5:")
print(f"Path: {path2_bfs}")
print(f"Time taken: {time2_bfs:.6f} seconds")
print(f"Memory usage: {memory2_bfs} bytes\n")

# Test on Graph 2 (Example Two) using DFS
path2_dfs, time2_dfs, memory2_dfs = measure_performance(dfs_shortest_path, graph2, '1', '5')
print("Example Two: Graph 2 - DFS Shortest path from 1 to 5:")
print(f"Path: {path2_dfs}")
print(f"Time taken: {time2_dfs:.6f} seconds")
print(f"Memory usage: {memory2_dfs} bytes")
