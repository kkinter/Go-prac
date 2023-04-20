import sys

sys.stdin = open("input.txt")

def bseaerch(arr, target):
    st = 0
    en = m - 1
    res = -1
    while st <= en:
        mid = (st + en) // 2

        if arr[mid] < target:
            res = mid
            st = mid + 1
        else:
            en = mid - 1
    return res

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    nlist = sorted(list(map(int, input().split())))
    mlist = sorted(list(map(int, input().split())))
    cnt = 0

    for i in nlist:
        cnt += bseaerch(mlist, i) + 1
    
    print(cnt)