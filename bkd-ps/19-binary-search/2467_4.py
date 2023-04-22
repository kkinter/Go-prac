import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

val = float("INF")
x, y = 0, 0
l = 0
r = n - 1

while l < r:
    cur = liquids[l] + liquids[r]

    if abs(cur) <= val:
        x = liquids[l]
        y = liquids[r]
        val = abs(cur)

    if cur <= 0:
        l += 1
    
    else:
        r -= 1

print(x, y)