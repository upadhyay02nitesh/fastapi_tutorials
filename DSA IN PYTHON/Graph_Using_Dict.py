class Graph:
    def __init__(self,vno):
        self.vertex_num=vno 
        self.adj_dict={v:[] for v in range(vno)}

    def add_edge(self,u,v):
        if 0<=u<self.vertex_num and 0<=v<self.vertex_num:
            self.adj_dict[u].append(v)
            self.adj_dict[v].append(u)
        else:
            print("Invalid vertices")
    
        
    def print_edge(self):
        for i,j in self.adj_dict.items():
            print("V",i,":",j)
    
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_num and 0<=v<self.vertex_num:
            if v in self.adj_dict[u]:
                self.adj_dict[u].remove(v)
            if u in self.adj_dict[v]:
                self.adj_dict[v].remove(u)
        else:
            print("Invalid Vertices !!!")


    

    def has_edge(self,u,v):
        if 0<=u<self.vertex_num and 0<=v<self.vertex_num:
            for i in self.adj_dict[u]:
                if i==v:
                    return True 
            return False
        else:
            print("Invalid vertices")
    
   

        
    
    
    

g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(3,4)
g.print_edge()
print()
print(g.remove_edge(1,4))
g.print_edge()


