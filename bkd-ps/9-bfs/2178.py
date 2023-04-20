import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    que = deque([(x, y)])
    visitedCnt[x][y] = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if mazeMatrix[nx][ny] == '1' and not visitedCnt[nx][ny]:
                    que.append([nx, ny])
                    visitedCnt[nx][ny] += 1 + visitedCnt[x][y]




n, m = map(int, input().split())
mazeMatrix = [list(input().rstrip('\n')) for _ in range(n)]
visitedCnt = [[0] * m for _ in range(n)]
bfs(0, 0)
print(visitedCnt[-1][-1])
