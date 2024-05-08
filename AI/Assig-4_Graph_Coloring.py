import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def is_safe(self, v, color, c):
        for i in range(self.vertices):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graph_coloring_backtracking(self, color_set):
        color = [None] * self.vertices
        self._graph_coloring_util_backtracking(color_set, color, 0)
        num_colors_used = len(set(color))
        print("Minimum number of colors used (Backtracking):", num_colors_used)
        print("Graph coloring:")
        for i, c in enumerate(color):
            print(f"Vertex {i} colored with: {c}")

    def _graph_coloring_util_backtracking(self, color_set, color, v):
        if v == self.vertices:
            return True

        for c in color_set:
            if self.is_safe(v, color, c):
                color[v] = c
                if self._graph_coloring_util_backtracking(color_set, color, v + 1):
                    return True
                color[v] = None

    def graph_coloring_branch_and_bound(self, color_set):
        def bound(v):
            max_used_color = max(color[:v]) if v > 0 else 0
            return max_used_color

        def _graph_coloring():
            pq = [(0, [-1] * self.vertices)]
            while pq:
                used_colors, coloring = heapq.heappop(pq)
                v = coloring.index(-1) if -1 in coloring else self.vertices
                if v == self.vertices:
                    return coloring

                for c in color_set:
                    if self.is_safe(v, coloring, c):
                        new_coloring = list(coloring)
                        new_coloring[v] = c
                        heapq.heappush(pq, (used_colors + 1, new_coloring))

        coloring = _graph_coloring()
        num_colors_used = len(set(coloring))
        print("Minimum number of colors used (Branch and Bound):", num_colors_used)
        print("Graph coloring:")
        for i, c in enumerate(coloring):
            print(f"Vertex {i} colored with: {c}")

def main():
    vertices = int(input("Enter the number of vertices in the graph: "))
    g = Graph(vertices)
    print("Enter the adjacency matrix of the graph:")
    for i in range(vertices):
        row = list(map(int, input().split()))
        for j in range(vertices):
            g.graph[i][j] = row[j]

    while True:
        print("\nSelect the method to solve the graph coloring problem:")
        print("1. Backtracking")
        print("2. Branch and Bound")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            color_set = input("Enter the set of colors separated by space: ").split()
            g.graph_coloring_backtracking(color_set)
        elif choice == '2':
            color_set = input("Enter the set of colors separated by space: ").split()
            g.graph_coloring_branch_and_bound(color_set)
        else:
            print("Invalid choice. Please enter '1' or '2'.")

        stop = input("Do you want to stop? (yes/no): ").lower()
        if stop == "yes":
            break

if __name__ == "__main__":
    main()
