import sys

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or matrix[i][j] != 1:
        return 0

    visited[i][j] = True
    area = 1
    area += dfs(i + 1, j)
    area += dfs(i - 1, j)
    area += dfs(i, j + 1)
    area += dfs(i, j - 1)
    return area


sys.stdin = open('./input.txt')

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for x in range(m)] for y in range(n)]

pt_cnt = 0 # 그림의 개수
max_area = 0 # 그림의 넓이
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not visited[i][j]:
            pt_cnt += 1
            area = dfs(i, j)
            max_area = max(max_area, area)

print(pt_cnt)
print(max_area)