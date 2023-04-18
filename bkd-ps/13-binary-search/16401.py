import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

m, n = map(int, input().split())
nums = list(map(int, input().split()))

def binary(arr, res):
    st = 0
    en = max(nums)

    while st <= en:
        cnt = 0 
        mid = (st + en) // 2
        
        if mid == 0:
            cnt = 0
            break

        for i in arr:
            cnt += i // mid

        if cnt >= m:
            st = mid + 1
            res = mid
        else:
            en = mid - 1
    return res

print(binary(nums, 0))

        