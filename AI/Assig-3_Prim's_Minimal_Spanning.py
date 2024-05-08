import sys

class Graph():
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printMST(self,parent):
        print("Edge \tWeight")
        for i in range(1,self.V):
            print(parent[i],'-',i,self.graph[i][parent[i]])

    def minkey(self,key,mstSet):
        min_val = sys.maxsize
        min_index = None
        for v in range(self.V):
            if key[v]<min_val and not mstSet[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        for cout in range(self.V):
            u = self.minkey(key,mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v]>0 and not mstSet[v] and key[v]>self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.printMST(parent)

if __name__ == '__main__':
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    print("Enter the adjacent matrix: ")
    for i in range(vertices):
        g.graph[i] = list(map(int,input().split()))
    g.primMST()
