import sys
import heapq
sys.stdin = open("input.txt")

input = sys.stdin.readline
n = int(input())
heap = [[] for x in range(n)]
sum = 0
for i in range(n):
    deadline, cup = map(int, input().split())
    heapq.heappush(heap[deadline - 1], (-cup, deadline))
max_sum = 0
cur_sum = 0
for j in range(n):
    if len(heap[j]) > 0:
        cur = heapq.heappop(heap[j])[0]
        day_sum = cur
        cur_sum =  cur_sum + cur
        for _ in range(1,len(heap[j])):
            day_sum +=  heapq.heappop(heap[j])[0]

        max_sum += max(cur_sum, day_sum)

print(max_sum)
