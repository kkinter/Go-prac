import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))

bridge = [0] * w
t = 0

while bridge:
    t += 1
    bridge.pop(0)
    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
print(t)
    

