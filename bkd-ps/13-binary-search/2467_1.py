import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

ans = float("INF")
ans_left = 0
ans_right = 0

for i in range(n - 1):
    cur = liquids[i]

    st = i + 1
    en = n - 1

    while st <= en:
        mid = (st + en) // 2
        tmp = cur + liquids[mid]

        if abs(tmp) < ans:
            ans = abs(tmp)
            ans_left = i
            ans_right = mid

            if tmp == 0:
                break

        if tmp < 0:
                st = mid + 1
            
        else:
             en = mid - 1

print(liquids[ans_left], liquids[ans_right])