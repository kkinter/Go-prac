from pprint import pprint
from collections import deque
import sys
sys.stdin = open("input.txt")


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def bfs(x, y):
    q = deque([(x, y)])
    tmp = [(x, y)]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[nx][ny]-graph[x][y]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    tmp.append((nx, ny))
    return tmp


res = 0

while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                countries = bfs(i, j)

                if len(countries) > 1:
                    flag = True
                    number = sum(graph[x][y]
                                 for x, y in countries) // len(countries)
                    for x, y in countries:
                        graph[x][y] = number
    if not flag:
        break

    res += 1

print(res)
