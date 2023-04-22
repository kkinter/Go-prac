import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

upFloor = [0 for _ in range(20)]
dp = [0 for _ in range(20)]

for i in range(n):
    upFloor[i] = int(input())

dp[0] = upFloor[0]
dp[1] = upFloor[0] + upFloor[1]
dp[2] = max(upFloor[1] + upFloor[2], upFloor[0] + upFloor[2])

for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + upFloor[i - 1] + upFloor[i], dp[i - 2] + upFloor[i])
    # dp[i - 3] + upFloor[i - 1] + upFloor[i] 마지막 계단의 전 단계를 밟은 경우
    # dp[i - 2] + upFloor[i] 마지막 계단의 전 계단을 밟지 않은 경우
    print(dp)
print(dp[i - 1])