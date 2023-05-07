import sys
from collections import defaultdict

sys.stdin = open("input.txt")
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

l, r = 0, k - 1

dict = defaultdict(int)
dict[c] += 1
# defaultdict(<class 'int'>, {30: 2, 7: 2, 9: 1})

for i in range(r + 1):
    dict[sushi[i]] += 1

res = float("-INF")

while l < n:
    res = max(len(dict), res)
    # 왼쪽 접시 제거
    dict[sushi[l]] -= 1
    if dict[sushi[l]] == 0:
        del dict[sushi[l]]

    l += 1
    r += 1
    dict[sushi[r % n]] += 1

print(res)
