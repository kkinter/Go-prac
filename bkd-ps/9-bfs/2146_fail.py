import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline 

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def findContinent(x, y):
    que = deque([(x, y)])
    visited[x][y] = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if islandMap[nx][ny] == 1:
                    que.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
    return (x, y)

n = int(input())
islandMap = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
continents = []
for i in range(n):
    for j in range(n):
        if islandMap[i][j] == 1 and not visited[i][j]:
            st = (i, j)
            en = findContinent(i, j)
            continents.append([st, en])
print(continents)