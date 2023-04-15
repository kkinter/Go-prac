def dfsRr(v, visited, path):
    visited[v] = True
    path.append(v)
    print(v, path)

    for w in graph[v]:
        if not visited[w]:
            dfsRr(w, visited, path)
    
    if v == path[-1]:
        print(' -> '.join(str(i) for i in path))

    path.pop()
    return visited

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]


visited = [False] * 9
for i in range(9):
    if not visited[i]:
        dfsRr(i, visited, [])


