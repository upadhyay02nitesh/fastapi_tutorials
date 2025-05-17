class Graph:
    def __init__(self,vno):
        self.vertex_num=vno 
        self.adj_dict={key:[] for key in range(vno)}

    def add_edge(self,u,v):
        if 0<=u<self.vertex_num and 0<=v<self.vertex_num:
            self.adj_dict[u].append(v)
            self.adj_dict[v].append(u)
        else:
            print("Invalid vertices")
    
        
    def print_edge(self):
        for i,j in self.adj_dict.items():
            print("V",i,":",j)
    
    def BFS(self):
        visited = []
        queue = []

        # Start BFS traversal from each vertex
        for vertex in range(self.vertex_num):
            # If the vertex has not been visited yet
            if vertex not in visited:
                # Append the vertex to the visited list and the queue
                visited.append(vertex)
                queue.append(vertex)

                # BFS traversal
                while queue:
                    temp = queue.pop(0)
                    print(temp, end=" ")

                    # Visit all neighbors of the current vertex
                    for neighbor in self.adj_dict[temp]:
                        if neighbor not in visited:
                            visited.append(neighbor)
                            queue.append(neighbor)

            
        

g=Graph(6)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(3,4)


g.print_edge()
print()
g.BFS()