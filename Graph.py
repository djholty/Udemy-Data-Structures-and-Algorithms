from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])
        
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                return False
            return True
        return False

    def bfs(self, vertex):#O(V+E) time complexity and OV space
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue: #O(V)
            current_vertex = queue.popleft() #popping out element from python list is O-N time complexity.. if you use deque is has better time complexity *double ended queue
            print(current_vertex, "-->", sep="", end ="")
            for adjacent_vertex in self.adjacency_list[current_vertex]:#O(E) time complexity
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)



custom_graph = Graph()
custom_graph.add_vertex('A')
custom_graph.add_vertex("B")
custom_graph.add_vertex("C")
custom_graph.add_vertex("D")
custom_graph.add_edge('A', 'C')
custom_graph.add_edge('A', 'B')
custom_graph.add_edge('B', 'C')

custom_graph.print_graph()
custom_graph.remove_edge('A',"C")
custom_graph.print_graph()
print(custom_graph.remove_edge("A", 'D'))
custom_graph.bfs('A')
 
