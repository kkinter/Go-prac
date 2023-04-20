import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color):
    que = deque([(x, y)])
    visited[x][y] = True

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if area[nx][ny] in color:
                    que.append([nx, ny])
                    visited[nx][ny] = True

n = int(input())
area = [list(input().rstrip('\n')) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

res ={
    "R": 0,
    "G": 0,
    "B": 0,
    "RG": 0,
      }
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, area[i][j])
            res[area[i][j]] += 1
res2 ={
    "B": 0,
    "RG": 0,
      }

visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if area[i][j] in "RG":
                bfs(i, j, "RG")
                res2["RG"] += 1
            else:
                bfs(i, j, area[i][j])
                res2[area[i][j]] += 1
            

print(sum(res.values()), sum(res2.values()))
