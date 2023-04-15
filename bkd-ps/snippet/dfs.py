import collections

def dfsR(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfsR(graph, i, visited)

def dfsRr(v, visited, path):
    visited[v] = True
    path.append(v)

    for w in graph[v]:
        if not visited[w]:
            dfsRr(w, visited, path)
    
    if v == path[-1]:
        print(' -> '.join(str(i) for i in path))

    path.pop()
    return visited

visited = [False] * 9
for i in range(9):
    if not visited[i]:
        dfsRr(i, visited, [])


def dfs(graph, start):
    visited = [False] * 9
    stack = [start]

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v, end=" ")
            for i in graph[v]:
                stack.append(i)

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


dfs(graph, 1)
print()
dfsRr(1, visited, [])