import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    que = deque([(x, y)])
    visited[x][y] = True

    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and farmArea[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append([nx, ny])


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    farmArea = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        farmArea[y][x] = 1

    insectCnt = 0
    for i in range(n):
        for j in range(m):
            if farmArea[i][j] == 1 and not visited[i][j]:
                insectCnt += 1
                bfs(i, j)
    print(insectCnt)
    