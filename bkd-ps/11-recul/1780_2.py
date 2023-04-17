import sys
from pprint import pprint

def check(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if mat[x][y] != mat[i][j]:
                return False
    return True

def sol(x, y, z):
    if check(x, y, z):
        res[mat[x][y] + 1] += 1
        return
    n = z // 3
    for i in range(3):
        for j in range(3):
            sol(x+i*n, y+j*n, n)


sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
res = [0] * 3
sol(0, 0, N)
for r in res:
    print(r)