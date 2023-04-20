import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, k = map(int, input().split())
max = 100001
dist = [0] * max
move = [0] * max

actionQ = deque([n])
while actionQ:
    x = actionQ.popleft()
    if x == k:
        print(dist[x])
        arr = []
        tmp = x
        for _ in range(dist[x] + 1):
            arr.append(tmp)
            tmp = move[tmp]
        print(*arr[::-1])
        break

    for i in (x + 1, x - 1, 2 * x):
        if 0 <= i < max and dist[i] == 0:
            actionQ.append(i)
            dist[i] = dist[x] + 1
            move[i] = x
