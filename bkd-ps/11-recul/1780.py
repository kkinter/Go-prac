import sys
from pprint import pprint

sys.stdin = open("input.txt")

def check(x, y, n):
    cur = mat[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if cur != mat[i][j]:
                return False
    return True

def solve(x, y, z):
    if check(x, y, z):
        res[mat[x][y] + 1] += 1
        return
    t = z // 3

    for i in range(3):
        for j in range(3):
            solve(x+i*t, y+j*t, t)

n = int(input())
mat = [[] for _ in range(n)]
res = [0] * 3
for i in range(n):
    mat[i] = list(map(int,input().split()))

solve(0, 0, n)

print(res)



