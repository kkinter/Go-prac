import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))

ans_left = 0
ans_right = 0
val = float("INF")
l = 0
r = n - 1

while l < r:
    cur = solutions[l] + solutions[r]

    if abs(cur) <= val:
        ans_left = l
        ans_right = r
        val = abs(cur)

    if cur <= 0:
        l += 1
    else:
        r -= 1

print(ans_left, ans_right)
