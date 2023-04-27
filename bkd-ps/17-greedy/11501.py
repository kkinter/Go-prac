import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))
    res = 0
    max_val = 0
    for i in range(n-1, -1, -1):
        if stocks[i] > max_val:
            max_val = stocks[i]
        elif stocks[i] < max_val:
            res += max_val - stocks[i]
    print(res)


        