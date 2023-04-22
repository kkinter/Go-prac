import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bsearch(arr, target):
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

a, b = map(int, input().split())
anums = list(map(int ,input().split()))
bnums = sorted(list(map(int ,input().split())))
res = []

for num in anums:
    if not bsearch(bnums, num):
        res.append(num)
print(len(res))
if len(res) != 0:
    print(*sorted(res))
