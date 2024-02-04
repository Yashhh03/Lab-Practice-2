def bfs(graph, start_node):
    visited = []
    queue = []

    visited.append(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

graph = {}
nodes = int(input("Enter the number of nodes: "))

for i in range(nodes):
    node = input(f"Enter node {i + 1}: ")
    neighbors = input(f"Enter neighbors for node {node} (comma-separated, press Enter if none): ")
    graph[node] = neighbors.split(',')

start_node = input("Enter the starting node: ")

print("Following is the Breadth-First Search:")
bfs(graph, start_node)

