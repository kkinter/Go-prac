import sys
import copy
sys.stdin = open("input.txt")


def fill(matrix, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break

            if matrix[nx][ny] == 6:
                break

            elif matrix[nx][ny] == 0:
                matrix[nx][ny] = "#"


def dfs(depth, matrix):
    global min_value
    if depth == len(cctv_list):
        count = 0
        for i in range(n):
            count += matrix[i].count(0)
        min_value = min(min_value, count)
        return

    tmp = copy.deepcopy(matrix)
    cctv_num, x, y = cctv_list[depth]

    for i in mode[cctv_num]:
        fill(tmp, i, x, y)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(matrix)


n, m = map(int, input().split())
cctv_list = []
matrix = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    matrix.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv_list.append((data[j], i, j))

min_value = float("INF")
dfs(0, matrix)
print(min_value)
