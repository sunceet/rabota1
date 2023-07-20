def find_paths(graph, start, end, path=[]):
    # Добавляем текущую вершину в путь
    path = path + [start]
    
    # Если текущая вершина является целью, добавляем путь к списку всех путей
    if start == end:
        return [path]
    
    # Если текущая вершина не существует в графе, возвращаем пустой список
    if start not in graph:
        return []
    
    # Рекурсивно ищем пути от соседних вершин до целевой вершины
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    
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

all_paths = find_paths(graph, start, end)
print(f"Все пути от вершины {start} до вершины {end}:")
for path in all_paths:
    print(' -> '.join(path))
