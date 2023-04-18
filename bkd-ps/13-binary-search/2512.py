import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
total = int(input())

if sum(arr) <= total:
    print(max(arr))
else:
    min_val = min(arr)
    max_val = max(arr)

def search(arr, target):
    l, r  = min_val, max_val
    s = sum(arr)

    while l <= r:
        mid = s // 2

        if arr[mid] > target:
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            return mid
    return False