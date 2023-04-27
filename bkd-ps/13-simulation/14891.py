import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

gearmap = {}

def rotate(deq, direction):
    if direction == 1:
        deq.appendleft(deq.pop())
    else:
        deq.append(deq.popleft())
    return deq

for i in range(4):
    gearmap[i+1] = deque(list(input().rstrip('\n')))

k = int(input())

for _ in range(k):
    num, direction = map(int, input().split())
    
    l, r = num-1, num+1

    while l > 0:
        tmp = direction
        if gearmap[l][2] != gearmap[l+1][6]:
            rotate(gearmap[l], -tmp)
            tmp = -tmp
        l -= 1 

    while r < 4:
        tmp = direction
        if gearmap[r-1][2] != gearmap[r][6]:
            rotate(gearmap[r], -tmp)
            tmp = -tmp
        r += 1

    rotate(gearmap[num], direction)

res = 0
for i in range(1, 5):
    res += 2**int(gearmap[i][0])
print(res)





