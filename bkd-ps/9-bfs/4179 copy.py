import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, input().split())
mazeMatrix = [list(input().rstrip('\n')) for _ in range(c)]

fireDist = [[-1 for _ in range(r)] for _ in range(c)]
curDist = [[-1 for _ in range(r)] for _ in range(c)]

jhCoordinate = []
fireCoodinate = []


for i in range(c):
    for j in range(r):
        if mazeMatrix[i][j] == 'J':
            jhCoordinate.append([i,j])
            curDist[i][j] = 0
        elif mazeMatrix[i][j] == 'F':
            fireCoodinate.append([i,j])
            fireDist[i][j] = 0

fireQ = deque(fireCoodinate)
curQ = deque(jhCoordinate)

while fireQ:
    x, y = fireQ.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 불이 좌표 밖으로 나갔을 때
        if nx < 0 or nx >= c or ny < 0 or ny > r:
            continue 
        
        # 이미 방문했거나, 벽일 경우
        if fireDist[nx][ny] != -1 or mazeMatrix[nx][ny] == "#":
            continue

        fireDist[nx][ny] = fireDist[x][y] + 1
        fireQ.append([nx, ny])

while curQ:
    x, y = curQ.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= c or ny < 0 or ny >= r:
            print(curDist[x][y] + 1)
            exit()
        
        if curDist[nx][ny] != -1 or mazeMatrix[nx][ny] == "#":
            continue

        if curDist[x][y] + 1 >= fireDist[nx][ny] and fireDist[nx][ny] != -1:
            continue

        curQ.append([nx, ny])
        curDist[nx][ny] = curDist[x][y] + 1
        
print("IMPOSSILE")