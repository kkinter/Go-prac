import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
matrix = [list(map(int, input().rstrip('\n'))) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
q = deque([(0, 0, False)])

visited[0][0][0] = 1
while q:
    x, y, flag = q.popleft()
    if x == n - 1 and y == m - 1:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            # 벽을 부수지 않은 경우
            if matrix[nx][ny] == 0 and not flag and visited[nx][ny][0] == 0:
                q.append((nx, ny, False))
                visited[nx][ny][0] = visited[x][y][0] + 1
            # 벽을 부수고 이동하는 경우
            elif matrix[nx][ny] == 1 and not flag and visited[nx][ny][1] == 0:
                q.append((nx, ny, True))
                visited[nx][ny][1] = visited[x][y][0] + 1
            # 이미 벽을 부순 상태인 경우
            elif matrix[nx][ny] == 0 and flag and visited[nx][ny][1] == 0:
                q.append((nx, ny, True))
                visited[nx][ny][1] = visited[x][y][1] + 1

if visited[n - 1][m - 1][0] == 0 and visited[n - 1][m - 1][1] == 0:
    print(-1)
elif visited[n - 1][m - 1][0] != 0 and visited[n - 1][m - 1][1] != 0:
    print(min(visited[n - 1][m - 1]))
else:
    print(max(visited[n - 1][m - 1]))