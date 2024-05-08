class Graph():
    def __init__(self,vertices):
        self.V= vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printMST(self,dist):
        print("vertex \tDistance from source")
        for i in range(self.V):
            print(i,'\t\t',dist[i])

    def minkey(self,dist,mstSet):
        min_val = float('inf')
        min_index = None
        for v in range(self.V):
            if dist[v] < min_val and not mstSet[v]:
                min_val = dist[v]
                min_index = v
        return min_index

    def dijstra(self,src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        mstSet = [False] * self.V
        for _ in range(self.V):
            u = self.minkey(dist,mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and not mstSet[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.printMST(dist)

if __name__ == '__main__':
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    print("Enter the adjacent matrix: ")
    for i in range(vertices):
        g.graph[i] = list(map(int,input().split()))
    source_vertex = int(input("Enter the source vertex: "))
    g.dijstra(source_vertex)
