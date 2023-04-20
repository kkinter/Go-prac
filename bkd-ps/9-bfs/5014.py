import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

# 총 f 층 스타트링크 g, 강호 위치 s 
f, s, g, u, d = map(int, input().split())
delta = [u, -d]
visited = [0] * (f + 1)

def bfs():
    que = deque([(s)])
    visited[s] = 1

    while que:
        dx = que.popleft()

        for d in delta:
            nx = dx + d

            if 1 <= nx <= f and not visited[nx]:
                visited[nx] = visited[dx] + 1
                que.append(nx)
    

bfs()
if not visited[g]:
    print('use the stairs')
else:
    print(visited[g] - 1)

