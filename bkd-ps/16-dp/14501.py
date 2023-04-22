import sys
sys.stdin = open("input.txt")

n = int(input())
tasks = [(0, 0, 0)] # cargo 
for i in range(n):
    t, p = map(int, input().split())
    tasks.append((t, p, i+1))

days = 7 # capacity
dp = [[0 for _ in range(days + 1)] for _ in range(n + 1)]  # pack

for i in range(1, n + 1):
    for j in range(1, days + 1):
        tskTime = dp[i][0]
        tskValue = dp[i][1]
        tskStart = dp[i][2]

        if tskTime <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - tskTime] + tskValue)
        else:
            dp[i][j] = dp[i-1][j]

print(dp)