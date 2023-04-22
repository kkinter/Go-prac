import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, c = map(int, input().split())
homelist = sorted([int(input()) for x in range(n)])

def binary_search(arr, st, en):
    while st <= en:
        mid = (st + en) // 2
        cur = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] >= cur + mid:
                count += 1
                cur = arr[i]
        
        if count >= c:
            global answer
            st = mid + 1
            answer = mid
        else:
            en = mid - 1

st = 1
en = homelist[-1] - homelist[0]
answer = 0
