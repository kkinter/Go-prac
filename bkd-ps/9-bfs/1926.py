import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline 

from pprint import pprint
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, cnt):
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if mat[nx][ny] == 1:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append([nx, ny])
    return cnt


n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
islandCnt = 0
maxArea = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] != 0 and not visited[i][j]:
            islandCnt += 1
            maxArea = max(maxArea, bfs(i, j, 1))
print(islandCnt, maxArea, sep='\n')