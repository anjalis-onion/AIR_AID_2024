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

def get_path(previous, end):
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous[node[0], node[1]]
    path.reverse()
    return path

def dijkstra_with_steps(grid, start, end):
    rows, cols = grid.shape
    distance = np.full((rows, cols), np.inf)
    previous = np.full((rows, cols), None)
    distance[start] = 0
    
    # Priority queue (min-heap)
    queue = []
    heapq.heappush(queue, (0, start))
    
    path_steps = []  # List to capture steps for animation

    distances = {}  # Dictionary to store distances

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        x, y = current_node
        
        if (x, y) == end:
            break
        
        # Add the current distance to distances dictionary
        distances[(x, y)] = current_distance
        
        # Add the current state to path_steps
        path_steps.append({'path': get_path(previous, end)})
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 4-connected neighbors
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx, ny] == 0:
                new_distance = current_distance + 1
                if new_distance < distance[nx, ny]:
                    distance[nx, ny] = new_distance
                    previous[nx, ny] = (x, y)
                    heapq.heappush(queue, (new_distance, (nx, ny)))
    
    # Final step to add the last path state
    path_steps.append({'path': get_path(previous, end)})
    
    return path_steps, distances


def visualize_distance(grid, distances, filename="distance_map.png"):
    fig, ax = plt.subplots()
    distance_matrix = np.full(grid.shape, np.nan) #initialize matrix
    for (x, y), distance in distances.items():
        distance_matrix[x, y] = distance
    cax = ax.imshow(distance_matrix, cmap='viridis', interpolation='nearest')
    fig.colorbar(cax, ax=ax, label='Distance from start') #add color bar
    plt.savefig(filename)
    plt.show()

def visualize_path(grid, path, filename="output.png"):
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
    start = (0, 0)
    end = (grid.shape[0] - 1, grid.shape[1] - 1)
    
    path_steps, distances = dijkstra_with_steps(grid, start, end)
    
    # Extract the final path
    final_path = path_steps[-1]['path']
    
    # Generate and save the distance map
    visualize_distance(grid, distances, filename="distance_map.png")
    
    # Generate and save the path map
    visualize_path(grid, final_path, filename="path_map.png")