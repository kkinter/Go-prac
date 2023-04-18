import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

ans = float('INF')
ans_left = 0
ans_right = 0

for i in range(n - 1):
    cur = liquids[i]
    l, r = i + 1, n - 1
    
    while l <= r:
        mid = (l + r) // 2
        tmp = cur + liquids[mid]

        if abs(tmp) < ans:
            print(l, r, i, mid)
            ans_left = i
            ans_right = mid
            ans = abs(tmp)

            if tmp == 0:
                break
        
        if tmp < 0:
            l = mid + 1
        else:
            r = mid - 1

print(liquids[ans_left], liquids[ans_right])
