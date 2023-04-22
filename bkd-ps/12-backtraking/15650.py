import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def comb(depth, n, m):
    if depth == m and sorted(ans) not in res:
        res.append(ans[:])
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            comb(depth+1, n, m)
            visited[i] = False
            ans.pop()


n, m = map(int, input().split())
visited = [False] * (n + 1)
ans = []
res = []
comb(0, n, m)
for i in res:
    print(*i)