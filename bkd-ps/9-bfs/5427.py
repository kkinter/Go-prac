import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

t = int(input())
for _ in range(t):
    w,h = map(int, input().split())
    buildingMap = [list(input().rstrip('\n')) for _ in range(h)]
    
    fireDist = [[-1] * w for _ in range(h)]
    curDist = [[-1] * w for _ in range(h)]
    
    fireQ = deque()
    curQ = deque()
    flag = False

    for i in range(h):
        for j in range(w):
            if buildingMap[i][j] == '@':
                curQ.append([i, j])
                curDist[i][j] = 0
            elif buildingMap[i][j] == '*':
                fireQ.append([i, j])
                fireDist[i][j] = 0

    while fireQ:
        x, y = fireQ.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if buildingMap[nx][ny] == '#' or fireDist[nx][ny] >= 0:
                continue
            fireDist[nx][ny] = fireDist[x][y] + 1
            fireQ.append([nx, ny])
    
    while curQ:
        x, y = curQ.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                print(curDist[x][y] + 1)
                flag = True
                break

            if curDist[nx][ny] >= 0 or buildingMap[nx][ny] == '#':
                continue

            if fireDist[nx][ny] != -1 and fireDist[nx][ny] <= curDist[x][y] + 1:
                continue

            curDist[nx][ny] = curDist[x][y] + 1
            curQ.append([nx, ny])
        else:
            continue
        break

    if not flag:
        print("IMPOSSIBLE")


# print(*fireDist, sep='\n')
# print()
# print(*curDist, sep='\n')