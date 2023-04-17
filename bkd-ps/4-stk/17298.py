import sys

sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))
stk = []
res = [-1] * n
for i, v in enumerate(arr):
    while stk and v > arr[stk[-1]]:
        lst = stk.pop()
        res[lst] = v

    stk.append(i)

print(*res)
