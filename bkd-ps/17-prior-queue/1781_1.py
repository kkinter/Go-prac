import sys
import heapq

sys.stdin = open("input.txt")

input = sys.stdin.readline
n = int(input())

task_heap = []
total_sum = 0

for i in range(n):
    deadline, cups = map(int, input().split())
    heapq.heappush(task_heap, (deadline, -cups))

result = 0
time = 1
min_cups = []

while task_heap:
    cur_task = heapq.heappop(task_heap)
    result -= cur_task[1]
    heapq.heappush(min_cups, -cur_task[1])

    if task_heap and time == task_heap[0][0]:
        while task_heap and cur_task[0] == task_heap[0][0]:
            next_task = heapq.heappop(task_heap)

            if -next_task[1] > min_cups[0]:
                result -= heapq.heappop(min_cups)
                result -= next_task[1]
                heapq.heappush(min_cups, -next_task[1])
    time += 1

if result >= 2**31:
    print(2**31)
else:
    print(result)