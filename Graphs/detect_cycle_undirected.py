from collections import defaultdict

class Graph:
    def __init__(self, V) -> None:
        self.graph = defaultdict(list)
        self.V = V 
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def isCyclicUtil(self, visited, vertex, parent):
        visited[vertex] = True
        for neighbour in self.graph[vertex]:
            if not visited[neighbour]:
                return self.isCyclicUtil(visited, neighbour, vertex)
            elif neighbour!=parent:
                return True
        return False
    
    def isCyclic(self):
        visited = [False]*self.V
        for vertex in range(self.V):
            if not visited[vertex]:
                if self.isCyclicUtil(visited, vertex, -1):
                    return True
        return False
if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(0, 3)
    g.addEdge(3, 4)
    print(g.isCyclic())