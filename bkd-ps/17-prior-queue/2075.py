import sys
import heapq
sys.stdin = open("input.txt")

input = sys.stdin.readline
que = []
n = int(input())
for i in range(n):
    row = list(map(int, input().split()))
    for j in row:
        if len(que) >= n:
            if que[0] < j:
                heapq.heappop(que)
                heapq.heappush(que, j)
        else:
            heapq.heappush(que, j)

print(heapq.heappop(que))

