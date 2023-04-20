import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(ripeTomatoes):
    que = deque()
    for tomato in ripeTomatoes:
        x, y = tomato
        que.append([x, y])

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and tomatoBox[nx][ny] == 0:
                tomatoBox[nx][ny] = tomatoBox[x][y] + 1
                que.append([nx, ny])
        

    

m, n = map(int, input().split())
tomatoBox = [list(map(int, input().split())) for _ in range(n)]
#visited = [[False for _ in range(m)] for _ in range(n)]
ripeTomatoes = []
for i in range(n):
    for j in range(m):
        if tomatoBox[i][j] == 1:
            ripeTomatoes.append((i, j))

bfs(ripeTomatoes)
flag = False
rst = float("-INF")

for i in range(n):
    for j in range(m):
        if tomatoBox[i][j] == 0:
            flag = True
        rst = max(tomatoBox[i][j], rst)

if flag:
    print(-1)
else:
    print(rst - 1)
