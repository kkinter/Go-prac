import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def perm(depth, n, m):
    if depth == m:
        res.append(tmp[:])
        return
    
    for i in range(len(nlist)):
        if not visited[i]:
            tmp.append(nlist[i])
            visited[i] = True
            perm(depth+1, n, m)
            tmp.pop()
            visited[i] = False
        
    

n, m = map(int, input().split())
nlist = sorted(list(map(int, input().split())))
visited = [False] * (n + 1)
tmp = []
res = []
perm(0, n, m)
for r in res:
    print(*r)
