class Graph:
    def __init__(self,vno):
        self.vno=vno 
        self.adj_dict={i:[] for i in range(vno)}
    
    def add_edge(self,u,v):
        if 0<=u<self.vno and 0<=v<self.vno:
            self.adj_dict[u].append(v)
            self.adj_dict[v].append(u)
        else:
            print("Invalid Vertices!!!")

    def remove_edge(self,u,v):
        if 0<=u<self.vno and 0<=v<self.vno:
            if v in self.adj_dict[u]:
                self.adj_dict[u].remove(v)
            if u in self.adj_dict[v]:
                self.adj_dict[v].remove(u)
            
        else:
            print("Invalid Vertices!!!")
    
    def has_edge(self,u,v):
        if 0<=u<self.vno and 0<=v<self.vno:
            for i in self.adj_dict[u]:
                if i==v:
                    return True
            return False
        else:
            print("Invalid Vertices!!!")

    
    
    def print_edge(self):
        for i,j in self.adj_dict.items():
            print("V",i,":",j)
    
    def dfs(self):
        visited = []
        stack = []

        # Start BFS traversal from each vertex
        for vertex in range(self.vno):
            # If the vertex has not been visited yet
            if vertex not in visited:
                # Append the vertex to the visited list and the queue
                visited.append(vertex)
                stack.append(vertex)

                # BFS traversal
                while stack:
                    temp = stack.pop()
                    print(temp, end=" ")

                    # Visit all neighbors of the current vertex
                    for neighbor in self.adj_dict[temp]:
                        if neighbor not in visited:
                            visited.append(neighbor)
                            stack.append(neighbor)
    

g=Graph(6)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(4,5)
g.print_edge()
print("*******************")
print(g.has_edge(0,3))
g.remove_edge(1,2)
g.print_edge()
g.dfs()