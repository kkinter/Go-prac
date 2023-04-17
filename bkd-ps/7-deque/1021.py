import sys
from collections import deque
sys.stdin = open("input.txt")

n, m = map(int, input().split())
nums = list(map(int, input().split()))
circle = deque([x for x in range(1, n + 1)])

cnt = 0
for i in nums:
    while True:
        if circle[0] == i:
            circle.popleft()
            break
        else:
            idx = circle.index(i)
            if idx <= len(circle) // 2:
                while circle[0] != i:
                    circle.append(circle.popleft())
                    cnt += 1
            else:
                while circle[0] != i:
                    circle.appendleft(circle.pop())
                    cnt += 1
print(cnt)



    
    