class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def bellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for count in range(self.V - 1):
            for u,v,w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        for u,v,w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        
        print("Distace from Source")
        for vertex, distance in enumerate(dist):
            print(f"{vertex} is {distance} distance away from {src}")

if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)
    print("Graph0")
    g.bellmanFord(0)

    g1 = Graph(4)
    g1.addEdge(0, 1, 1)
    g1.addEdge(1, 2, -1)
    g1.addEdge(2, 3, -1)
    g1.addEdge(3, 0, -1)
    print("Graph1")
    g1.bellmanFord(0)
 