from collections import defaultdict
class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        #Directed Graph
        self.graph[u].append(v)
    
    def BFS(self, start):
        visited =[False] * (max(self.graph)+1)

        q = []
        q.append(start)
        visited[start] = True
        result = []
        while q:
            popped = q.pop(0)
            result.append(popped)
            for i in self.graph[popped]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
        return  result

if __name__ == "__main__":
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(2, 0)
    graph.addEdge(1, 2)
    graph.addEdge(0, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)

    bfs = graph.BFS(2)
    print(*bfs, sep = "->")