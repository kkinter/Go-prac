import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
mazeMatrix = [list(input().rstrip('\n')) for _ in range(n)]
fireDist = [[-1 for _ in range(m)] for _ in range(n)]
curDist = [[-1 for _ in range(m)] for _ in range(n)]
fireQ = deque()
curQ = deque()


for i in range(n):
    for j in range(m):
        if mazeMatrix[i][j] == 'J':
            curQ.append([i,j])
            curDist[i][j] = 0
        elif mazeMatrix[i][j] == 'F':
            fireQ.append([i,j])
            fireDist[i][j] = 0

while fireQ:
    x, y = fireQ.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if fireDist[nx][ny] >= 0 or mazeMatrix[nx][ny] == "#":
            continue
        fireDist[nx][ny] = fireDist[x][y] + 1
        fireQ.append([nx, ny])

while curQ:
    x, y = curQ.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            print(curDist[x][y] + 1)
            exit(0)
        
        if curDist[nx][ny] >= 0 or mazeMatrix[nx][ny] == '#':
            continue

        if fireDist[nx][ny] != -1 and fireDist[nx][ny] <= curDist[x][y] + 1:
            continue

        curDist[nx][ny] = curDist[x][y] + 1
        curQ.append([nx, ny])

print("IMPOSSIBLE")