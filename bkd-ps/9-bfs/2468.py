import sys
from collections import deque
from heapq import heappush
sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    que = deque([(x, y)])
    visited[x][y] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and area[nx][ny] - l > 0:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append([nx, ny])


n = int(input())
area = []
min_height = float("INF")
max_height = float("-INF")
for i in range(n):
    row = list(map(int, input().split()))
    min_height = min(min_height, min(row))
    max_height = max(max_height, max(row))
    area.append(row)
l, r = min_height, max_height
rst = []
while l <= r:
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] - l > 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    rst.append(cnt)
    l += 1

if len(rst) == 1 and rst[0] == 0:
    print(1)
else:
    print(max(rst))

