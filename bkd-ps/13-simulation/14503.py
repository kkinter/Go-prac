import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(x, y):
    need = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and roomMatrix[nx][ny] == 0:
            need = True
    return need
    
def bfs(x, y, d):
    q = deque([(x, y)])
    # 현재 칸을 청소한다.
    visited[x][y] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        
        if check(x, y):
            while True:
                d = (d - 1) % 4
                nx = x + dx[d]
                ny = y + dy[d]
                print(d)
                if roomMatrix[nx][ny] == 0:
                    break
            
            if 0 <= nx < n and 0 <= ny < m and roomMatrix[nx][ny] == 0 and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = True
        else:
            d = (d + 2) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and roomMatrix[nx][ny] == 0 and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = True
            elif  0 <= nx < n and 0 <= ny < m and roomMatrix[nx][ny] == 1:
                print(d, nx, ny)
                return


n, m = map(int, input().split())
x, y, d = map(int, input().split())
roomMatrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]


bfs(x, y ,d)



from pprint import pprint

pprint(visited)