import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    buildingMap = []
    for i in range(l):
        floorMap = [list(input().replace('\n', '')) for _ in range(r + 1)]
        buildingMap.append(floorMap[:r])
    visitedMap = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]

    stQ = deque()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if buildingMap[i][j][k] == 'S':
                    stQ.append([i, j, k])
                    visitedMap[i][j][k] = 0
                elif buildingMap[i][j][k] == 'E':
                    tz, ty, tx = i, j ,k

    while stQ:
        z, y, x = stQ.popleft()

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or nx >= c or ny < 0 or ny >= r or nz < 0 or nz >= l:
                continue
            
            if visitedMap[nz][ny][nx] >= 1 or buildingMap[nz][ny][nx] == '#':
                continue

            stQ.append([nz, ny, nx])
            visitedMap[nz][ny][nx] = visitedMap[z][y][x] + 1

    if visitedMap[tz][ty][tx] > 0:
        print(f"Escaped in {visitedMap[tz][ty][tx]} minute(s).")
    else:
        print("Trapped!")


