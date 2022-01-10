from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def DFSUtil(self, source, visited: list[bool], result):
        result.append(source)
        visited[source] = True
        for neighbour in self.graph[source]:
            if not visited[neighbour]:
                self.DFSUtil(neighbour, visited, result)
    def DFS(self, source):
        visited = [False] * (max(self.graph)+1)
        result = []
        self.DFSUtil(source, visited, result)
        return result
    
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    dfs = g.DFS(2)

    print(*dfs, sep = "->")