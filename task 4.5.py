def find_paths(graph: dict, current_node: str, end: str, path=[]):

    path = path + [current_node]

    if current_node == end:
        return [path]

    paths = []

    for node in graph[current_node]:
        new_paths = find_paths(graph, node, end, path)
        paths.extend(new_paths)

    return paths


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
end = 'F'

paths = find_paths(graph, start, end)
print(f'All ways from {start} to {end}: {paths}')
