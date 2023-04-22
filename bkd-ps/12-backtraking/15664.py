import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def perm(depth, n, m):
    if depth == m and sorted(tmp) == tmp:
        res.append(tmp[:])
        return 
    
    prev = 0
    for i in range(n):
        if not visited[i] and prev != nlist[i]:
            visited[i] = True
            tmp.append(nlist[i])
            prev = nlist[i]
            perm(depth+1, n, m)
            visited[i] = False
            tmp.pop()


n, m = map(int, input().split())
nlist = sorted(list(map(int, input().split())))
visited = [False] * n
res = []
tmp = []

perm(0, n, m)
for r in res:
    print(*r)