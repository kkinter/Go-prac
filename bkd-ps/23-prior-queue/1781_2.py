import sys
import heapq

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    deadline, cupNoodle = map(int, input().split())
    array.append((deadline, cupNoodle))

array.sort()

queue = []

for i in array:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)
    print(queue, i, len(queue))
    
print(sum(queue))