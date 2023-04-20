import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m, l = map(int, input().split())
rests = [0] + sorted(list(map(int, input().split()))) + [l]

st = 1
en = l - 1
res = 0

while st <= en:
    mid = (st + en) // 2
    cnt = 0

    for i in range(1, len(rests)):
        if rests[i] - rests[i - 1] >= mid:
            cnt += (rests[i] - rests[i - 1] - 1) // mid
        
    if cnt > m:
        st = mid + 1
    else:
        res = mid
        en = mid - 1

print(res)
