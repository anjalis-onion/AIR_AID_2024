# SUPPORT U 
# Smart UAV Program for the Population by Offering Resources and Tools to the Unhoused

## Dependicies:
### pip3 install numpy
### pip3 install matplotlib 

## Purpose:

### Team Air Aid's project revolves around a drone system which navigates a city, and delivers hygiene kits to homeless people. In order for succesful pathfinding from the drone's current location to the center of operations, an efficient and reliable pathfinding algorithm is required. After analyzing A-star algorithm, Dijkstra's algorithm, and Depth First Search algorithm, it is evident that Dijkstra's algorithm is the most reliable and optimal option. The dijkstra.py file shows an example implementation of this algorithm. Two different figures will also serve as a visual aid; The first one demonstrates a distance map and the second one displays the shortest path. 

## Visuals

The path map shows the route found by Dijkstra's algorithm from the start point to the endpoint.

![Path Map](code_Imgs/path_map.png)

The distance map visualizes the distance from the start point to every other point on the grid.

![Distance Map](code_Imgs/distance_map.png)

## CSV File Input and pathfinding

### The csv file is in the form of a matrix. One's in the matrix resemble obstacles, while zeros resemble empty spaces. The program is currently set to always start at the top left corner and finish at the bottom right, but this can be changed.

## Output

### The file will reuturn the path that it follows like so:
### Path: [[0 0]
###   [1 0]
###   [2 0]
###   [2 1]
###   [2 2]
###   [2 3]
###   [2 4]
###   [2 5]
###   [3 5]
###   [4 5]
###   [5 5]
###   [5 6]
###   [5 7]
###   [6 7]
###   [7 7]
###   [8 7]]
