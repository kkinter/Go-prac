import sys
sys.stdin = open("input.txt")

n = int(input())
tasks = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

# for i in range(n):
#     for j in range(i + tasks[i][0], n + 1):
#         if dp[j] < dp[i] + tasks[i][1]:
#             dp[j] = dp[i] + tasks[i][1]

# print(dp)

for i in range(n-1, -1, -1):
    if i + tasks[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], tasks[i][1] + dp[i + tasks[i][0]])
    print(dp)
print(dp[0])