import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

m, n = map(int, input().split())
nums = list(map(int, input().split()))

st = 0
en = max(nums)

res = 0
while st <= en:
    cnt = 0
    mid = (st + en) // 2

    if mid == 0:
        res = 0
        break

    for i in nums:
        if i >= mid:
            cnt += i // mid
    
    if cnt >= m:
        st = mid + 1
        res = mid
    else:
        en = mid - 1

print(res)