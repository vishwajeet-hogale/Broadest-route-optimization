def sort_queue(queue): # [node_number,cost]
    return sorted(queue,key = lambda x : x[1], reverse = True)
def ucs(graph,n,start,goal):
    max_dis = -1
    max_path = ""
    queue = []
    visited = [0 for i in range(n)]
    queue.append([start,0,str(start)]) # add the start to the queue 
    # graph1 = graph
    while(len(queue) != 0):
        queue = sort_queue(queue)
        curr_node = queue[0][0]
        cost = queue[0][1]
        path = queue[0][2]
        queue.pop(0)
        visited[curr_node] = 1
        for neigh in range(n):
            if(neigh == goal ):
                # graph1[curr_node][neigh] = -2
                if(max_dis<cost + graph[curr_node][neigh]):
                    max_dis = cost + graph[curr_node][neigh]
                    max_path = path + ", " + str(neigh)
                continue
            if(graph[curr_node][neigh] not in [0,-1] and visited[neigh] == 0):
                # graph1[curr_node][neigh] = -3
                queue.append([neigh,cost+graph[curr_node][neigh],path + ", " + str(neigh)]) 
            # print(graph1)      
            # print()         
    return max_path,max_dis
def get_path(graph,n,start,goal):
    max_dis = -1
    max_path = ""
    queue = []
    visited = [0 for i in range(n)]
    queue.append([start,0,str(start)]) # add the start to the queue 
    # graph1 = graph
    while(len(queue) != 0):
        queue = sort_queue(queue)
        curr_node = queue[0][0]
        cost = queue[0][1]
        path = queue[0][2]
        queue.pop(0)
        visited[curr_node] = 1
        for neigh in range(n):
            if(neigh == goal ):
                # graph1[curr_node][neigh] = -2
                if(max_dis<cost + graph[curr_node][neigh]):
                    max_dis = cost + graph[curr_node][neigh]
                    max_path = path + ", " + str(neigh)
                continue
            if(graph[curr_node][neigh] not in [0,-1] and visited[neigh] == 0):
                # graph1[curr_node][neigh] = -3
                queue.append([neigh,cost+graph[curr_node][neigh],path + ", " + str(neigh)]) 
            # print(graph1)      
            # print()         
    return max_path.split(",")
if __name__ == "__main__":
    # graph = [[0,0,0,0,0,0,0],
    #          [0,0,0,2,0,1,0],
    #          [0,0,0,0,0,0,9],
    #          [0,0,0,0,8,0,3],
    #          [0,0,0,0,0,10,0],
    #          [0,0,0,0,0,0,1],
    #          [0,0,0,0,0,0,0]]
    
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
    
    # dis,path = ucs(graph,7,1,6)
    dis,path = ucs(graph,11,1,3)
    print(dis)
    print(path)