import sys
from pprint import pprint
sys.stdin = open("input.txt")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
seat_plan = [[0]*n for _ in range(n)]
students = [list(map(int, input().split())) for _ in range(n**2)]

for seat in range(n**2):
    student = students[seat]
    tmp = []
    for i in range(n):
        for j in range(n):
            if seat_plan[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if seat_plan[nx][ny] in student[1:]:
                            like += 1
                        if seat_plan[nx][ny] == 0:
                            blank += 1
                tmp.append([like, blank, i, j])
    tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    seat_plan[tmp[0][2]][tmp[0][3]] = student[0]

res = 0
students.sort()

for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if seat_plan[nx][ny] in students[seat_plan[i][j] - 1]:
                    ans += 1
        if ans != 0:
            res += 10 ** (ans - 1)

print(res)
