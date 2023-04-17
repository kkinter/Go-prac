import sys
import collections

sys.stdin = open("input.txt")
input = sys.stdin.readline
n = int(input())
height = []

for i in range(n):
    height.append(int(input()))
res = 0
stk = []

for j in range(n):
    # 해당 건물 보다 높이가 작으면 stk 에서 pop
    while stk and height[j] > height[stk[-1]]:
        print(stk)
        lst = stk.pop()

    stk.append(j)

    res += len(stk) - 1

print(res)

        