import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def comb(depth, n, m):
    if depth == m:
        res.append(tmp[:])
        return
    prev = 0
    for i in range(n):
        if not visited[i] and prev != nlist[i]:
            tmp.append(nlist[i])
            visited[i] = True
            prev = nlist[i]
            comb(depth+1, n, m)
            visited[i] = False
            tmp.pop()



n, m = map(int, input().split())
nlist = sorted(list(map(int, input().split())))
visited = [False] * (n)
tmp = []
res = []
comb(0, n, m)
for i in res:
    print(*i)