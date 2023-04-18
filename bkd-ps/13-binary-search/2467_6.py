import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

ans = float("INF")
ans_left = 0
ans_right = 0
l = 0
r = n - 1

while l < r:
    cur = liquids[l] + liquids[r]

    if abs(cur) <= ans:
        ans_left = l
        ans_right = r
        ans = abs(cur)

    if cur <= 0:
        l += 1
    else:
        r -= 1

print(liquids[ans_left], liquids[ans_right])