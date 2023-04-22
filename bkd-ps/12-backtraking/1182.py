import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, s = map(int, input().split())
nlist = list(map(int, input().split()))
cnt = 0
ans = []

def solve(start):
    global cnt
    if sum(ans) == s and len(ans) > 0:
        cnt += 1

    for i in range(start, n):
        ans.append(nlist[i])
        solve(i+1)
        ans.pop()

solve(0)
print(cnt)
