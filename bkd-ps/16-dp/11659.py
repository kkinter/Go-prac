import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = list(map(int, input().split()))

dp = [0 for _ in range(n + 1)]

dp[1] = nlist[0]
for k in range(2, n + 1):
    dp[k] = dp[k - 1] + nlist[k - 1]

for i in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])


# [0, 5, 9, 12, 14, 15]