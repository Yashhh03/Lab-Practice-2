def create_graph():
    graph = {}
    while True:
        node = input("Enter a node (or 'exit' to finish): ")
        if node.lower() == 'exit':
            break
        neighbors = input(f"Enter neighbors for node {node} separated by spaces: ").split()
        graph[node] = neighbors
    return graph

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

graph = create_graph()
visited = set()

start_node = input("Enter the starting node for DFS: ")
print("Following is the Depth-First Search")
dfs(visited, graph, start_node)

