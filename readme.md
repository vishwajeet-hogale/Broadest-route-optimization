# Route Optimization
This code defines a function `tri_Traversal` that performs three different graph traversals: Depth-First Search (DFS), Uniform Cost Search (UCS), and A* search. The function takes input parameters such as the cost matrix (`cost`), heuristic list (`heuristic`), starting node (`start_point`), and a list of goal nodes (`goals`).

The code also includes three separate functions for each traversal algorithm: `dfs`, `ucs`, and `a_star`. These functions implement the logic for DFS, UCS, and A* search, respectively.

## Here's a brief explanation of each traversal function:

1. **DFS (`dfs`):**
   - It uses a stack to perform depth-first traversal.
   - The `stack` contains the nodes to be explored.
   - It maintains a `came_from` dictionary to keep track of the parent node for each explored node.
   - The traversal continues until all goals are reached.

2. **UCS (`ucs`):**
   - It uses a priority queue (implemented as a list) based on the cost to perform uniform cost search.
   - The priority queue is sorted based on the accumulated cost so far.
   - It also maintains a `came_from` dictionary and updates the cost so far for each explored node.
   - The traversal continues until all goals are reached.

3. **A* (`a_star`):**
   - It is similar to UCS but uses a heuristic function to prioritize nodes.
   - The priority is calculated as the sum of the cost so far and the heuristic value for each node.
   - It uses a priority queue sorted based on the priority.
   - The traversal continues until all goals are reached.

The `tri_Traversal` function calls these three traversal functions and returns a list containing the paths obtained from each traversal.

The code also includes some utility functions like `Sort_Tuple`, `check`, `pop`, and `calc_min` that are used within the traversal functions for sorting tuples, checking the existence of an element in a list of tuples, popping elements from the priority queue, and calculating the minimum cost path, respectively.

The sample `cost` matrix and `heuristic` list are provided for testing the traversals with a graph. The function is then called with these inputs to obtain the paths for each traversal algorithm.








## Graph 
### Flow
- Input
    - Start node
    - Destination node

- Ucs algorithm : To calculate broadest road btw the above points 
    - distance 
    - width 

    - distance & width = 0.3*distance + 0.7*width [Graph edges]

- Use TomTom api to calibrate the route based on the route calculated by UCS algorithm. 

- Use Leaflet JS to show the simulation of UCS algorithm finding the broadest route.


