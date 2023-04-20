import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
matrix = [list(map(int, input().rstrip('\n'))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
q = deque([(0, 0, False)])

t = 10
visited[0][0] = 1
while q:
    x, y, flag = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if matrix[nx][ny] == 0:
                q.append([nx, ny, flag])
                visited[nx][ny] = visited[x][y] + 1

            elif matrix[nx][ny] == 1 and not flag:
                q.append([nx, ny, True])
                visited[nx][ny] = visited[x][y] + 1

if visited[n - 1][m - 1] == 0:
    print(-1)
else:
    print(visited[n - 1][m - 1])

from pprint import pprint
pprint(visited)