import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

delta = [
    (-1, -2),
    (1, -2),
    (-2, -1),
    (2, -1),
    (-2, 1),
    (2, 1),
    (-1, 2),
    (1, 2)
]
def bfs(x, y):
    que = deque([(x, y)])
    chessMap[x][y] = 0

    while que:
        x, y = que.popleft()
        if x == targetX and y == targetY:
            return chessMap[x][y]
        
        for i in range(8):
            nx = x + delta[i][0]
            ny = y + delta[i][1]

            if 0 <= nx < n and 0 <= ny < n:
                if not chessMap[nx][ny]:
                    chessMap[nx][ny] = chessMap[x][y] + 1
                    que.append([nx, ny])

    

t = int(input())
for _ in range(t):
    n = int(input())
    chessMap = [[0 for _ in range(n)] for _ in range(n)]
    curX, curY = map(int, input().split())
    targetX, targetY = map(int, input().split())
    cnt = 0
    
    print(bfs(curX, curY))