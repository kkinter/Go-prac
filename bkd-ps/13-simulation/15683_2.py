import sys
import copy
sys.stdin = open("input.txt")

n, m = map(int, input().split())
cctvs = []
matrix = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]


def fill(matrix, directions, x, y):
    for direction in directions:
        nx = x
        ny = y
        while True:
            nx += dx[direction]
            ny += dy[direction]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break

            if matrix[nx][ny] == 6:
                break

            elif matrix[nx][ny] == 0:
                matrix[nx][ny] = "#"


def dfs(depth, matrix):
    global min_val

    if depth == len(cctvs):
        count = 0
        for row in range(n):
            count += matrix[row].count(0)
        min_val = min(min_val, count)
        return

    tmp = copy.deepcopy(matrix)
    cctv_num, x, y = cctvs[depth]

    for i in directions[cctv_num]:
        fill(tmp, i, x, y)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(matrix)


for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    for j in range(m):
        if row[j] in [1, 2, 3, 4, 5]:
            cctvs.append((row[j], i, j))

min_val = float("INF")
dfs(0, matrix)
print(min_val)
