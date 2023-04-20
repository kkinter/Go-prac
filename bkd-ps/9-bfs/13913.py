import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

def path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = moveidx[temp]
    print(' '.join(map(str, arr[::-1])))

n, k = map(int, input().split())
max = 40
dist = [0] * max 
moveidx = [0] * max


actionQ = deque()
actionQ.append(n)

while actionQ:
    x = actionQ.popleft()
    if x == k:
        print(dist[x])
        path(x)
        break

    dx = (x + 1, x - 1, x * 2)
    for i in range(3):
        nx = dx[i]
        if 0 <= nx < max and not dist[nx]:
            actionQ.append(nx)
            dist[nx] = dist[x] + 1
            moveidx[nx] = x

