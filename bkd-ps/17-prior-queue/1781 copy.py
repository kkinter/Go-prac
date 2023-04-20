import sys
import heapq
sys.stdin = open("input.txt")

input = sys.stdin.readline
n = int(input())
tasks = []
for i in range(n):
    deadline, cup = map(int, input().split())
    tasks.append((deadline, cup))

tasks.sort()
q = []

for task in tasks:
    heapq.heappush(q, task[1])
    if task[0] < len(q):
        heapq.heappop(q)
print(q)
