import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def n_and_m(depth, n, m):
    if depth == m:
        res.append(tmp[:])
        return
    prev = 0
    for i in range(n):
        if prev != nlist[i]:
            tmp.append(nlist[i])
            prev = nlist[i]
            n_and_m(depth+1, n, m)
            tmp.pop()

n, m = map(int, input().split())
nlist = sorted(list(map(int, input().split())))

res = []
tmp = []
n_and_m(0, n, m)

for r in res:
    print(*r)