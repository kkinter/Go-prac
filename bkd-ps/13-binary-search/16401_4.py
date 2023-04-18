import sys
sys.stdin = open("input.txt")

m, n = map(int, input().split())
l = list(map(int, input().split()))

def solve(x):
    if x == 0:
        return True
    cnt = 0
    for i in range(n):
        cnt += l[i] // x
    return cnt >= m

st = 0
en = max(l)

while st < en:
    mid = (st + en + 1) // 2
    if solve(mid):
        st = mid
    else:
        en = mid - 1

print(st)