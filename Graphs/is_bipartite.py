#Problem - https://leetcode.com/problems/is-graph-bipartite/

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def isBipartite(self) -> bool:
        n = max(self.graph)+1
        colorRef = [-1]*(n)
        for i in range(n):
            if colorRef[i] == -1:
                colorRef[i] = 1
                if not self.isBipartiteUtil(colorRef, i):
                    return False
        return True
    def isBipartiteUtil(self, colorRef, source):
        for neighbour in self.graph[source]:
            if colorRef[neighbour] == -1:
                colorRef[neighbour] = 1-colorRef[source]
                if not self.isBipartiteUtil(colorRef, neighbour):
                    return False
            elif colorRef[neighbour] == colorRef[source]:
                return False
        return True

if __name__ == "__main__":
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    print(graph.isBipartite())