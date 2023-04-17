import sys
from pprint import pprint
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt")

def check(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if mat[x][y] != mat[i][j]:
                return False
    return True

def sol(x, y, z):
    global res
    if check(x, y, z):
        res += mat[x][y]
        
        return
    
    n = z // 2

    res += '('
    for i in range(2):
        for j in range(2):
            sol(x + i*n, y + j*n, n)
    res += ')'
            


input = sys.stdin.readline
n = int(input())
mat = [list(input().strip("\n")) for _ in range(n)]
res = ""
sol(0, 0, n)
pprint(res)