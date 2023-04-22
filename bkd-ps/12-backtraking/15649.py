import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline



def comb(depth, n, m):
    if depth == m:
        res.append(ans[:])
        return
    
    for i in range(1, n+1):
        if not visitied[i]:
            ans.append(i)
            visitied[i] = True
            comb(depth+1, n, m)
            visitied[i] = False
            ans.pop()

n, m = map(int, input().split())
visitied = [False] * (n + 1)
ans = []
res = []
comb(0, n, m)
for i in res:
    print(*i)