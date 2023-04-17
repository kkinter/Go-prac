import sys
sys.stdin = open("input.txt")

def check(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[x][y] != paper[i][j]:
                return False
    return True

def solve(x, y, z):
    if check(x, y, z):
        cnt[paper[x][y]+1] += 1
        return
    n = z // 3
    for i in range(3):
        for j in range(3):
            solve(x+i*n, y+j*n, n)

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = [0]*3
solve(0, 0, N)
for i in range(3):
    print(cnt[i])