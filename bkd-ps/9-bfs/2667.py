import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, cnt):
    que = deque([(x, y)])
    visited[x][y] = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and houseMatrix[nx][ny] == '1':
                if not visited[nx][ny]:
                    que.append([nx, ny])
                    visited[nx][ny] = 1
                    cnt += 1
    return cnt


n = int(input())
houseMatrix = [list(input().rstrip('\n')) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
complexCnt = 0
res = []
for i in range(n):
    for j in range(n):
        if houseMatrix[i][j] == '1' and not visited[i][j]:
            res.append(bfs(i, j, 1))
            complexCnt += 1
print(complexCnt, *sorted(res), sep='\n')
