import sys
import pprint

sys.stdin = open('./input.txt')

n, k = map(int, input().split())
arr = [[0 for x in range(2)] for s in range(6)]
res = 0

for i in range(n):
    s, y = map(int, input().split())
    arr[y - 1][s] += 1
    if arr[y - 1][s] % k == 0:
        res += arr[y - 1][s] / k
        arr[y - 1][s] = 0

for i in range(6):
    for j in range(2):
        if arr[i][j] % k == 0:
            res += arr[i][j] / k
        else:
            res += arr[i][j] // k + 1
print(int(res))