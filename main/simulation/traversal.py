import pandas as pd
import numpy as np
import heapq


def dijkstra_with_path(adj_matrix, source,target):
    """
    This function Implements Dijikstra's algorithm for graph traversal

    Parameters :
        adjacency_matrix -> np.ndarray : adjacency matrix for the weighted graph
        source -> int : source vertex

    returns :
        distances -> List[int] : distnace from each vertex to the source vertex
        predecessors -> dict[int,None] : predecessors of each vertext in the traversal
    """
    num_vertices = len(adj_matrix)
    distances = [float('infinity')] * num_vertices
    distances[source] = 0
    predecessors = [None] * num_vertices
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(num_vertices):
            if adj_matrix[current_vertex][neighbor] > 0:
                distance = current_distance + adj_matrix[current_vertex][neighbor]

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

    shortest_path = get_shortest_path(predecessors,target)

    return shortest_path


def bellman_ford(adjacency_matrix, source, target):
    """
    This function Implements bellman ford algorithm for graph traversal
    Parameters:
        adjacency_matrix -> np.ndarray : adjacency matrix for the weighted graph
        source -> int : source vertex

    Returns :
        path -> List[int] : Shortest path from source to destination
    """
    num_vertices = len(adjacency_matrix)
    distances = {vertex: float('infinity') for vertex in range(num_vertices)}
    predecessors = {vertex: None for vertex in range(num_vertices)}
    distances[source] = 0

    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v in range(num_vertices):
                weight = adjacency_matrix[u][v]
                if weight != 0 and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

    # Check for negative cycles
    for u in range(num_vertices):
        for v in range(num_vertices):
            weight = adjacency_matrix[u][v]
            if weight != 0 and distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative cycle")

    shortest_path = get_shortest_path(predecessors,target)

    return shortest_path


def uniform_cost_search(adjacency_matrix, source, target):
    """
    This function Implements Uniform Cost Search algorithm for graph traversal
    Parameters:
        adjacency_matrix -> np.ndarray : adjacency matrix for the weighted graph
        source -> int : source vertex

    Returns :
        path -> List[int] : Shortest path from source to destination
    """
    num_vertices = len(adjacency_matrix)
    distances = {vertex: float('infinity') for vertex in range(num_vertices)}
    predecessors = {vertex: None for vertex in range(num_vertices)}
    distances[source] = 0

    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in enumerate(adjacency_matrix[current_vertex]):
            if weight > 0:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct the path
    path = []
    current_vertex = target

    while current_vertex is not None:
        path.insert(0, current_vertex+1)
        current_vertex = predecessors[current_vertex]

    return path


def get_shortest_path(predecessors, target):
    """
    Parameters :
        predecessors -> Dict[int,int] : predecessors info from the traversal
        target -> int : Destination vertex
    
    Returns :
        path -> List[int] : Shortest path from source to destination
    """
    path = []
    current_vertex = target

    while current_vertex is not None:
        path.insert(0, current_vertex+1)
        current_vertex = predecessors[current_vertex]

    return path


def create_adjacency_matrix(edges_data, cost_function):
    """
    Parameters:
        edges_data -> pd.Dataframe : Edges data dataframe with source destination width and distnace

        cost_function -> (int,int) -> int : a cost calculation function that takes width and distance, returns a cost calculate using the defined formula

    returns adjacency matrix -> np.ndarray
    """
    nodes = set(edges_data['source']).union(set(edges_data['destination']))
    num_nodes = max(nodes)

    adjacency_matrix = np.zeros((num_nodes, num_nodes),dtype=float)

    for _, edge in edges_data.iterrows():
        source = int(edge['source']) - 1 
        destination = int(edge['destination']) - 1  
        width = edge['width']
        distance = edge['distance']
        adjacency_matrix[source, destination] = cost_function(width,distance) 
        adjacency_matrix[destination, source] = cost_function(width,distance)

    return adjacency_matrix


def min_max_scaling(column):
    """
    This function normalizes pd.Dataframe columns using min-max method

    parameters :
        Column -> pandas.DataFrame : column to be normalized
    
        Returns -> pandas.DataFrame :  Normalized column
    """
    min_val = column.min()
    max_val = column.max()

    if min_val == max_val:
        return column

    scaled_column = (column - min_val) / (max_val - min_val)
    return scaled_column


# Read graph data from excel file
def findpath(filename,start,end):
    excel_file_path = 'dataset4POC 3.xlsx'  # path of the excel file
    edges_data = pd.read_excel(excel_file_path,dtype={'source':int,'destination':int,'width':float,'height':float})

    # convert edge list into adjacency matrix
    # adjacency matrix with distnace as cost
    adjacency_matrix_distance = create_adjacency_matrix(edges_data, lambda width,distance: distance )

    # adjacency matrix with width as cost
    adjacency_matrix_width= create_adjacency_matrix(edges_data, lambda width,distance: width )

    # normalization of width and distance
    edges_data['distance'] = min_max_scaling(edges_data['distance'])
    edges_data['width'] = min_max_scaling(edges_data['width'])

    # adjacency matrix with normalized width and distance
    adjacency_matrix_width_dist = create_adjacency_matrix(edges_data,lambda x,y : (1.1-x)*y )
    adjacency_matrix_dist = create_adjacency_matrix(edges_data,lambda x,y : y )


    # define source and destination vertex
    source_vertex = start
    target_vertex = end

    # compute shortest path using bellman_ford or dijikstra's algorithm
    shortest_path_width_dist = uniform_cost_search(adjacency_matrix_width_dist, source_vertex, target_vertex)
    shortest_path_dist = uniform_cost_search(adjacency_matrix_dist, source_vertex, target_vertex)

    # computing total distance and average width of the route road
    dist_dist = 0
    width_sum_dist=0

    for i in range(len(shortest_path_dist)-1):
        dist_dist += adjacency_matrix_distance[shortest_path_dist[i]-1,shortest_path_dist[i+1]-1]
        width_sum_dist += adjacency_matrix_width[shortest_path_dist[i]-1,shortest_path_dist[i+1]-1]

    dist_width = 0
    width_sum_width=0

    for i in range(len(shortest_path_width_dist)-1):
        dist_width += adjacency_matrix_distance[shortest_path_width_dist[i]-1,shortest_path_width_dist[i+1]-1]
        width_sum_width += adjacency_matrix_width[shortest_path_width_dist[i]-1,shortest_path_width_dist[i+1]-1]

    avg_width_dist = round(width_sum_dist / len(shortest_path_width_dist),2)
    avg_width_width = round(width_sum_width / len(shortest_path_width_dist),2)
    # print(f"Source ( {source_vertex} ) to Destination ( {target_vertex} )")
    # print(f"Shortest distance  :  {dist}")
    # print(f"Average width  :  {avg_width}")
    print(f"Shortest path width distance: {shortest_path_width_dist}")
    print(f"Shortest path distance: {shortest_path_dist}")
    return {'width':dist_width,'dist':dist_dist}, {'dist':avg_width_dist,'width':avg_width_width}, shortest_path_width_dist, shortest_path_dist


