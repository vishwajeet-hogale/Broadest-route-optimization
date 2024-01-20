import random 
import ucs
import pandas as pd


"""
    Randomize the nodes. And create a dataset. 
"""

se_visited = {}
def encode_graph(graph):
    val = []
    for i in graph:
        for j in i:
            val.append(j)
    # print("".join(val))
    # print(val)
    return val
def create_datapoint(graph,n,g):
    # random.seed(random.randint(1,11))
    start_node = random.randint(5,11)
    end_node = random.randint(2,11)
    # start_node = 2
    # end_node = 9
    # if([start_node,end_node] not in se_visited):
    path = ucs.get_path(graph,11,start_node,end_node)
        # se_visited[[start_node,end_node]] = 1
    datapoints = []
    for i in range(len(path)-1):
        temp = [path[i],start_node,end_node,path[i+1]]
        temp = temp + g
        # temp = temp.append()
        # print(temp)
        datapoints.append(temp)
    print(datapoints)
    return datapoints

def randomize_create_dataset(graph):
    n = 1300
    g = encode_graph(graph)
    # print(g)
    dataset = []
    total_nodes = len(graph)
    while(n!=0):
        try:
            dp = create_datapoint(graph,total_nodes,g)
            if(len(dp) != 0):
                dataset.extend(dp)
        except: 
            continue
        n -= 1
        
    return dataset

if __name__ == "__main__":
    graph = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 5, 9, -1, 6, -1, -1, -1, -1, -1],
            [0, -1, 0, 3, -1, -1, 9, -1, -1, -1, -1], 
            [0, -1, 2, 0, 1, -1, -1, -1, -1, -1, -1],
            [0, 6, -1, -1, 0, -1, -1, 5, 7, -1, -1],
            [0, -1, -1, -1, 2, 0, -1, -1, -1, 2, -1],
            [0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
            [0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1],
            [0, -1, -1, -1, -1, 2, -1, -1, 0, -1, 8],
            [0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 7],
            [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]]
    
    dataset = randomize_create_dataset(graph)
    # print(dataset)
    df = pd.DataFrame(dataset,columns = ["D" + str(i) for i in range(len(dataset[0]))])
    # print(df.head())
    df.to_csv("RoutesData.csv")    
        