import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

t = int(input())
dp = [0] * 100
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(t):
    answer = int(input())
    for i in range(3, answer + 1):
        dp[i + 1] = dp[i - 2] + dp[i - 1] + dp[i] 
    print(dp[answer])
