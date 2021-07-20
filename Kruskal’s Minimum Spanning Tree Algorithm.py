from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []
        
    def addEdge(self,u,v,w):
        self.graph.append([w,u,v]) 
 
    def krushkalMST(self):
        visited = [False]*self.V
        self.graph = sorted(self.graph)
        mst=[] 

        for edge in self.graph:
            if visited[edge[1]] == False or visited[edge[2]] == False: 
                visited[edge[1]]=True
                visited[edge[2]]=True
                mst.append(edge)

        return mst

    def printGraph (self,mst):
        print("Minimum Spanning Tree for the given graph")
        weight=int(0)
        for edge in mst:
            print(edge[1],"--",edge[2]," = ",edge[0])
            weight+=edge[0]
        print("Total weight ",weight)


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

mst=g.krushkalMST()
g.printGraph(mst)
            
        
