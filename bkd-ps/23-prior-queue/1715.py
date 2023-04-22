import sys
import heapq
sys.stdin = open("input.txt")

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    x = int(input().strip('\n'))
    heapq.heappush(heap, x)

sum = 0

while len(heap) >= 2:
    l = heapq.heappop(heap)
    r = heapq.heappop(heap)
    sum += l + r
    heapq.heappush(heap, (l + r))

print(sum)