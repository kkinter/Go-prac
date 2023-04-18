import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
budget = int(input())

def binary(arr):
    st = 0
    en = max(arr)
    while st <= en:
        mid = (st + en) // 2
        cnt = 0
        for i in range(n):
            cnt += min(arr[i], mid)

        if cnt <= budget:
            st = mid + 1
        else:
            en = mid - 1
    return en
print(binary(arr))