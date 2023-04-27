import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

gearmap = {}

def check_right (st, dirs):
    if st > 4 or gearmap[st-1][2] == gearmap[st][6]:
        return
    
    if gearmap[st-1][2] != gearmap[st][6]:
        check_right(st+1, -dirs)
        gearmap[st].rotate(dirs)

def check_left (st, dirs):
    if st < 1 or gearmap[st][2] == gearmap[st+1][6]:
        return
    
    if gearmap[st+1][6] != gearmap[st][2]:
        check_left(st-1, -dirs)
        gearmap[st].rotate(dirs)

for i in range(1, 5):
    gearmap[i] = deque(list(map(int, input().rstrip('\n'))))

k = int(input())

for _ in range(k):
    num, direction = map(int, input().split())
    
    check_right(num+1, -direction)
    check_left(num-1, -direction)

    gearmap[num].rotate(direction)
    
    

result = 0
for i in range(4):
    result += (2**i) * gearmap[i+1][0]
print(result)



