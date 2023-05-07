import sys
from collections import defaultdict
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
passwordMap = defaultdict(str)

for _ in range(n):
    site, pwd = input().split()
    passwordMap[str(site)] = pwd

print(passwordMap)

for _ in range(m):
    s = input().rstrip('\n')
    print(passwordMap[s])
