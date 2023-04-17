import sys
from collections import deque, Counter

sys.stdin = open("input.txt")

t = int(input())
for i in range(t):
    p = input()
    n = int(input())
    law = input()
    if law == '[]':
        arr = []
    else:
        arr = deque(list(law.strip('[]').split(',')))
    flag = True
    rev = False
    c = Counter(p)
    if len(arr) < c['D']:
        flag = False
        print("error")
        continue
    else:
        for e in p:
            if e == 'R':
                if rev == True:
                    rev = False
                else:
                    rev = True
            elif e == 'D':
                if rev:
                    arr.pop()
                else:
                    arr.popleft()
    if rev:
        print("["+",".join(list(arr)[::-1])+"]")
    else:
        print("["+",".join(list(arr))+"]")
    
    


    



