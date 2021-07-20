class adjNode:
    def __init__(self,data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self,vertics):
        self.V = vertics
        self.graph=  [None]*self.V

    def add_edge(self,src,des):
        node = adjNode(des)
        node.next = self.graph[src]
        self.graph[src] = node

        node = adjNode(src)
        node.next = self.graph[des]
        self.graph[des] = node


    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print("->",temp.vertex ,end="")
                temp = temp.next
            print("\n")    


if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0,4)
    graph.add_edge(0,1)
    graph.add_edge(1,3)
    graph.add_edge(2,3)
    graph.add_edge(2,4)
    graph.print_graph()
    
