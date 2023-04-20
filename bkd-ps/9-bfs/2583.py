import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, cnt):
    que = deque([(x, y)])
    area[x][y] = 1


    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and area[nx][ny] == 0:
                area[nx][ny] = 1
                que.append([nx, ny])
                cnt += 1
    return cnt



m, n, k = map(int, input().split())
area = [[0 for _ in range(n)] for _ in range(m)]
visitied = [[False for _ in range(n)] for _ in range(m)]


for _ in range(k):
    leftX, leftY, rightX, rightY = map(int, input().split())
    for i in range(-(leftY + 1), -rightY -1, -1):
        for j in range(leftX, rightX):
            area[i][j] = -1
rst = []
divideCnt = 0
for i in range(m):
    for j in range(n):
        if area[i][j] == 0:
            rst.append(bfs(i, j, 1))
            divideCnt += 1
print(divideCnt)
print(*sorted(rst))