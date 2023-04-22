import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def perm(depth, n, m):
    if depth == m:
        res.append(tmp[:])
        return
    
    for i in range(len(nlist)):
        if len(tmp) >= 1 and nlist[i] < tmp[-1]:
            continue
        tmp.append(nlist[i])
        perm(depth+1, n, m)
        tmp.pop()

n, m = map(int, input().split())
nlist = sorted(list(map(int, input().split())))
tmp = []
res = []
perm(0, n, m)
for r in res:
    print(*r)