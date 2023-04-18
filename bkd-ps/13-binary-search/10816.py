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
            i, j = 1, 1
            while mid - i >= 0:
                if arr[mid - i] != arr[mid]:
                    break
                else: 
                    i += 1
            while mid + j <= len(arr) - 1:
                if arr[mid + j] != arr[mid]:
                    break
                else:
                    j += 1
            return i + j - 1 
    return -1

n = int(input())
nums1 = sorted(list(map(int, input().split())))
m = int(input())
nums2 = list(map(int, input().split()))
res = []
for num in nums2:
    c = search(nums1, num)
    if c != -1:
        res.append(c)
    else:
        res.append(0)
print(*res)


        
