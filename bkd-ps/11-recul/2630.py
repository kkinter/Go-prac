import sys
from pprint import pprint

def check(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if mat[i][j] != mat[x][y]:
                return False
    return True

def sol(x, y, z):
    if check(x, y, z):
        res[mat[x][y]] += 1
        return
    
    n = z // 2
    for i in range(2):
        for j in range(2):
            sol(x +i*n, y + j*n, n)


sys.stdin = open("input.txt")
input = sys.stdin.readline
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
res = [0] * 2

pprint(mat)