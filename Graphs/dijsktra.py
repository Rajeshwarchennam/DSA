from sys import maxsize
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0]*vertices for i in range(vertices)]
    def dijsktra(self, source):
        dist = [maxsize]*self.V
        spt = [False]*self.V
        dist[source] = 0
        for i in range(self.V):
            curr = self.minDistance(dist, spt)
            spt[curr] = True
            for j in range(self.V):
                if self.graph[curr][j] > 0 and spt[j] == False and \
                dist[j] > dist[curr] + self.graph[curr][j]:
                    dist[j] = dist[curr] + self.graph[curr][j]
        return dist
    def minDistance(self, dist, spt):
        mini = maxsize
        for i in range(self.V):
            if dist[i] < mini and spt[i] == False:
                mini = dist[i]
                minIndex = i
        return minIndex

if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
    shortestDistances = g.dijsktra(0)
    print(*enumerate(shortestDistances), sep="\n")

        