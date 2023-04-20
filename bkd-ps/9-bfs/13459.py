import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

x, y = map(int, input().split())
max = 1000001
visited = [False] * max

time = 0
actionQ = deque([(x, time)])

while actionQ:
    cur, time = actionQ.popleft()
    if cur == y:
        break
    visited[cur] = True
    curTeleport = cur * 2

    while 0 <= curTeleport < max and not visited[curTeleport]: 
        actionQ.append([curTeleport, time])
        visited[curTeleport] = True
        curTeleport *= 2

    dx = (cur + 1, cur - 1)
    for d in dx:
        if 0 <= d < max and not visited[d]:
            actionQ.append([d, time + 1])
            visited[d] = True
    time += 1
print(time)