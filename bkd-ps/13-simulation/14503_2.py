import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int,input().split())
graph = []
visited = [[False] * m for _ in range(n)]
r, c, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0 ,1 ,0, -1]

graph = [list(map(int, input().split())) for _ in range(n)]

visited[r][c] = 1
cnt = 1

while True:
    flag = False

    for _ in range(4):
        nx = r + dx[(d-1) % 4]
        ny = c + dy[(d-1) % 4]

        d = (d-1) % 4
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                cnt += 1
                r = nx
                c = ny

                flag = True
                break
            
    if flag == False:
        if graph[r -dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
        else:
            r,c = r-dx[d], c-dy[d]
