import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
res = 0
for i in range(len(coins)-1, -1, -1):
    res += k // coins[i]
    k = k % coins[i]
print(res)
