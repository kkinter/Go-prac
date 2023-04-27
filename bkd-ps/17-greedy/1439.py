import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = list(input())
prev = n[0]
res = [0, 0]
res[int(n[0])] = 1

for i in range(1, len(n)):
    if n[i] != prev:
        res[int(prev)] += 1
    prev = n[i]

print(min(res))