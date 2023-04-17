import sys

sys.stdin = open('input.txt')

n = int(input())
n_arr = list(map(int, input().split()))
x = int(input())

res = []
seen = dict()
for i in n_arr:
    t = x - i
    if i in seen.keys():
        res.append([i, t])
    else:
        seen[t] = i 
print(len(res))