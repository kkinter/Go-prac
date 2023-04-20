import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, k = map(int, input().split())
max = 100001
visited = [False] * max 
time = 0
path = [n]
actionQ = deque()
actionQ.append((n, time, len(path)))

while actionQ:
    x, curTime, curPathLen = actionQ.popleft()
    if x == k:
        print(curTime)
        print(*path[:curPathLen])
        break
    visited[x] = True

    dx = (x + 1, x - 1, x * 2)
    for i in range(3):
        nx = dx[i]

        if 0 <= nx < max and not visited[nx]:
            visited[nx] = True
            if len(path) < max:
                actionQ.append((nx, curTime + 1, curPathLen + 1))
                path.append(nx)