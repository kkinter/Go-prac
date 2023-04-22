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
            return True
    return False

n = int(input())
nums1 = sorted(list(map(int, input().split())))
m = int(input())
nums2 = list(map(int, input().split()))
res = []
for num in nums2:
    if search(nums1, num):
        res.append(1)
    else:
        res.append(0)
print(*res)