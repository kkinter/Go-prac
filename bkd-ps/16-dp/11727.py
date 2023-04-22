n = int(input())
dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    if i % 2 == 1:
        dp[i] = 2*(dp[i-1] - 1) + 1
    else:
        dp[i] = 2*(dp[i-1] - 1) + 3

print(dp[n] % 10007)


for i in range(2, n+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]