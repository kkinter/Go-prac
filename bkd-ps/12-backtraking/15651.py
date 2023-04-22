import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def perm(depth, n, m):
    if depth == m:
        res.append(ans[:])
        return
    
    for i in range(1, n+1):
        ans.append(i)
        perm(depth+1, n, m)
        ans.pop()

n, m = map(int, input().split())
ans = []
res = []
perm(0, n, m)
for i in res:
    print(*i)
