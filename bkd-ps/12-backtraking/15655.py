import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def comb(depth, n, m):
    if depth == m:
        if sorted(tmp) not in res:
            res.append(tmp[:])
        return
    
    for i in range(len(nlist)):
        if not visited[i]:
            tmp.append(nlist[i])
            visited[i] = True
            comb(depth+1, n, m)
            visited[i] = False
            tmp.pop()

n, m = map(int, input().split())
nlist = sorted(list(map(int, input().split())))
visited = [False] * (n + 1)
tmp = []
res = []
comb(0, n, m)
for r in res:
    print(*r)