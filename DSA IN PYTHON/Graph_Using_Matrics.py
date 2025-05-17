class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_mat=[[0]*vno for e in range(vno) ]

    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_mat[u][v]=weight
            self.adj_mat[v][u]=weight
        else:
            print("Invalid vertex")
        
    
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_mat[u][v]=0
            self.adj_mat[v][u]=0
        else:
            print("Invalid vertex")
        
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_mat[u][v]!=0
        else:
            print("Invalid vertex")
    
    def print_mat(self):
        for i in self.adj_mat:
            for s in i:
                print(s,end=" ")
            print()
g=Graph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.print_mat()

print()
print(g.has_edge(2,3))
g.remove_edge(0,1)
print()
g.print_mat()



        
        