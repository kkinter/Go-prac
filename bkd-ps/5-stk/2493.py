import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
n = int(input())
towers = list(map(int, input().split()))

res = [0] * n
stk = []

for i in range(n-1, -1, -1):
    while stk and towers[i] > towers[stk[-1]]:
        last = stk.pop()
        res[last] = i + 1
    stk.append(i)

print(*res)

