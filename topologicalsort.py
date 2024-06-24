from collections import defaultdict

class Graph:
    def __init__(self, numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices

    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        
        stack.insert(0,v)

    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)
        
        print(stack)

customgraph = Graph(8)
customgraph.addEdge("A", "C")
customgraph.addEdge("C", "E")
customgraph.addEdge("E", "H")
customgraph.addEdge("E", "F")
customgraph.addEdge("F", "G")
customgraph.addEdge("B", "D")
customgraph.addEdge("B", "C")
customgraph.addEdge("D", "F")

customgraph.topologicalSort()
