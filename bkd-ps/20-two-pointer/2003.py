import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

l, r = 0, 1
cnt = 0

while r <= n and l <= r:
    tmp = sum(nums[l:r])

    if tmp == m:
        cnt += 1
        r += 1

    elif tmp < m:
        r += 1

    else:
        l += 1

print(cnt)
