import sys
import heapq
sys.stdin = open("input.txt")

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    files = list(map(int, input().split()))
    heap = []
    for file in files:
        heapq.heappush(heap, file)
    sum = 0
    while len(heap) >= 2:
        l = heapq.heappop(heap)
        r = heapq.heappop(heap)
        sum += l + r
        heapq.heappush(heap, l+r)
    print(sum)
