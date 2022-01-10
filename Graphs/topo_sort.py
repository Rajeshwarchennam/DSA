from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def topoSort(self):
        visited = [False]*(max(self.graph)+1)
        stack = []
        for vertex in range(max(self.graph)+1):
            if not visited[vertex]:
                self.topoSortUtil(visited, stack, vertex)
        return stack[::-1]
    
    def topoSortUtil(self, visited, stack, source):
        visited[source] = True
        for neighbour in self.graph[source]:
            if not visited[neighbour]:
                self.topoSortUtil(visited, stack, neighbour)
        stack.append(source)

if __name__ == "__main__":
    g = Graph()
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(5, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.addEdge(4, 1)
    print(g.topoSort())