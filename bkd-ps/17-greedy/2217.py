import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
ropes = []
for i in range(n):
    ropes.append(int(input()))
ropes.sort()
res = 0

for i in range(n):
    res = max(res, ropes[i]*(n-i))
print(res)