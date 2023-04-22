import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bSearch(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return True
    return False

n = int(input())
nums1 = sorted(list(map(int, input().split())))
m = int(input())
nums2 = list(map(int, input().split()))

for num in nums2:
    if bSearch(nums1, num):
        print(1)
    else:
        print(0)
