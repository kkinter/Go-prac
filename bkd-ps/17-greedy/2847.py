import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
levels = [int(input()) for _ in range(n)]

cur = levels[-1]
res = 0
for i in range(n-1, 0,-1):
    if cur < levels[i-1]:
        res += levels[i-1] - cur + 1
        cur -= 1
    elif cur == levels[i-1]:
        res += 1
        cur -= 1
    else:
        cur = levels[i-1]


print(res)
