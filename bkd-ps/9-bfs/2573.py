import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input1.txt')
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def findIceberg(icebergMap):
    ices = []
    for i in range(n):
        for j in range(m):
            if icebergMap[i][j] > 0:
                ices.append([i, j])
    return ices


def melting(x, y, icebergMap):
    que = deque([(x, y)])
    visited[x][y] = True

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if icebergMap[nx][ny] > 0 and not visited[nx][ny]:
                que.append([nx, ny])
                visited[nx][ny] = True

            if icebergMap[nx][ny] == 0 and icebergMap[x][y] > 0 and not visited[nx][ny]:
                icebergMap[x][y] -= 1
    return icebergMap

n, m = map(int, input().split())
icebergMap = [list(map(int, input().split())) for _ in range(n)]
year = 0
oneFlag = False
while True:
    year += 1
    visited = [[False for _ in range(m)] for _ in range(n)]
    ices = findIceberg(icebergMap)
    chuckCnt = 0

    for ice in ices:
        x, y = ice
        if not visited[x][y]:
            melting(x, y, icebergMap)
            chuckCnt += 1

    if chuckCnt >= 2:
        break
    if len(ices) == 0:
        oneFlag = True
        break
if oneFlag:
    print(0)
else:
    print(year - 1)


