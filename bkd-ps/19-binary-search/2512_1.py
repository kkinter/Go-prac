import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solve(x):
    sum = 0
    for i in range(n):
        sum += min(arr[i], x)
    return budget >= sum

n = int(input())
arr = list(map(int, input().split()))
budget = int(input())

st = 0
en = max(arr)

while st < en:
    mid = (st + en) // 2
    if solve(mid):
        st = mid
    else:
        en = mid - 1
print(st)


