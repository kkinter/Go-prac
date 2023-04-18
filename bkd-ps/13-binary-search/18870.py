import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def search(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        
        if arr[mid] > target:
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            return mid
    return False

n = int(input())
x_arr = list(map(int, input().split()))
tmp = sorted(set(x_arr))
res = [0] * n

for i in range(n):
    res[i] = search(tmp, x_arr[i])
print(*res)
