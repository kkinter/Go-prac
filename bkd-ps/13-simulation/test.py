from time import time
from collections import deque


def compute_average(n):
    """Perform n appends to an empty list and return avg time elapsed."""
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n


"""
주어진 2차원 배열에서 값이 0인 데이터의 좌표만을 3개씩 묶어 중복이 없는 
조합의 형태로 나타내고 싶을 때, 어떻게 코딩하는것이 좋을까?
"""

n, m = 2, 2  # 가로, 세로
arr = [[0, 0], [0, 1]]  # 2차원 배열


def dfs(sx, sy, stack=[], result=[]):
    if len(stack) == 3:
        result.append(stack.copy())
        return

    for x in range(sx, n):
        sy = sy if x == sx else 0
        for y in range(sy, m):
            if arr[x][y] == 0:
                stack.append((x, y))
                dfs(x, y + 1, stack, result)
                stack.pop()

    return result


print(dfs(0, 0))


def dfs(depth, stack=[], result=[]):
    if len(stack) == 3:
        result.append(stack.copy())
        return

    for i in range(depth, n * m):
        # 1차원 배열의 i 를 2차원 배열로 변환
        x, y = i // m, i % m
        if arr[x][y] == 0:
            stack.append((x, y))
            dfs(i + 1, stack, result)
            stack.pop()
    return result


n = 3

cand = deque([(i, j) for i in range(n) for j in range(i % 2, n, 2)])
print(cand)
