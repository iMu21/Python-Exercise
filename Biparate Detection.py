from collections import defaultdict

class Graph:
    def __init__(self,vertict):
        self.graph = defaultdict(list)
        self.V = vertict
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def biparateCheck(self,visited,parent,val):
        visited[parent]=val
        for i in self.graph[parent]:
            if visited[i] == val:
                return False
            elif visited[i]==0:
                self.biparateCheck( visited,i,3-val)
        return True      

    def biparate(self):
        visited = [0]*self.V
        for i in range(self.V):
            if visited[i]==0:
               if  self.biparateCheck( visited,i,1) ==  False:
                   return False
        return True

g=Graph(5)

g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(1,2) 
g.add_edge(1,3) 
g.add_edge(4,2)
g.add_edge(4,3)
g.add_edge(4,0)  

if g.biparate():
    print("The graph is a Biparate Graph")
else:
    print("The graph is not a Biparate Graph")
    
        
