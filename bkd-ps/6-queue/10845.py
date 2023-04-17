from collections import deque
import sys
input = sys.stdin.readline

sys.stdin = open("input.txt")

n = int(input())
q = deque([])
for i in range(n):
    com = input().split()
    if com[0] == "push":
        q.append(com[1])
    elif com[0] == "pop":
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif com[0] == "size":
        print(len(q))
    elif com[0] == "empty":
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif com[0] == "front":
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif com[0] == "back":
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)
        
