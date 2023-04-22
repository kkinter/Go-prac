import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

floor = [0 for _ in range(20)]
dp = [0 for _ in range(20)]


for i in range(n):
    floor[i] = int(input())

dp[0] = floor[0]
dp[1] = floor[0] + floor[1]
dp[2] = max(floor[0] + floor[2], floor[1] + floor[2])

for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + floor[i - 1] + floor[i], dp[i - 2] + floor[i])

print(dp)