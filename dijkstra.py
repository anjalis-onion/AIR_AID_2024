import numpy as np
import matplotlib.pyplot as plt
import heapq
import csv

def load_grid_from_csv(filename):
    grid = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            grid.append([int(cell) for cell in row])
    return np.array(grid)

def neighbors(node, grid):
    x, y = node
    neighbor_positions = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    valid_neighbors = []
    for nx, ny in neighbor_positions:
        if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and grid[nx, ny] == 0:
            valid_neighbors.append((nx, ny))
    return valid_neighbors

def dijkstra(grid, start, end):
    queue = [(0, start)]
    distances = {start: 0}
    previous_nodes = {start: None}
    visited = set()
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        
        if current_node == end:
            break
        
        for neighbor in neighbors(current_node, grid):
            distance = current_distance + 1
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous_nodes[node]
    path.reverse()
    
    return path

def visualize(grid, path, filename="output.png"):
    fig, ax = plt.subplots()
    ax.imshow(grid, cmap=plt.cm.binary)

    if path:
        path = np.array(path)
        print("Path:", path)  # Print the path to confirm
        ax.plot(path[:, 1], path[:, 0], color='red', linewidth=2)
    
    plt.savefig(filename)
    plt.show()

if __name__ == "__main__":
    grid = load_grid_from_csv('grid_and_obstacles.csv')
    start = (0, 0)  # Starting point: top-left corner
    
    # Automatically determine the bottom-right corner as the end point
    end = (grid.shape[0] - 1, grid.shape[1] - 1)
    
    path = dijkstra(grid, start, end)
    visualize(grid, path)
