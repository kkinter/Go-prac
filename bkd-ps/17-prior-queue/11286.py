import sys
import heapq
sys.stdin = open("input.txt")

input = sys.stdin.readline
n = int(input())
que = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(que) > 0:
            print(heapq.heappop(que)[1])
        else:
            print(0)
    else:
        heapq.heappush(que, (abs(x), x))


    
