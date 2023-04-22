import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, c = map(int, input().split())
homelist = sorted([int(input()) for x in range(n)])

st, en = 1, homelist[-1] - homelist[0]
res = 0
if c == 2:
    print(homelist[-1] - homelist[0])
else:
    while st <= en:
        mid = (st + en) // 2
        cnt = 1
        ts = homelist[0]

        for i in range(n):
            if homelist[i] - ts >= mid:
                cnt += 1
                ts = homelist[i]

        if cnt >= c:
            res = mid
            st = mid + 1

        else:
            en = mid - 1
    print(res)