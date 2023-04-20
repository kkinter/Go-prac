import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
liquids = list(map(int ,input().split()))

value = float("INF")
ans_left, ans_right = 0, 0
l, r = 0, n - 1

while l < r:
    cur = liquids[l] + liquids[r]

    if abs(cur) <= value:
        ans_left = l 
        ans_right = r
        value = abs(cur)

    if cur < 0:
        l += 1

    else:
        r -= 1

print(liquids[ans_left] + liquids[ans_right])