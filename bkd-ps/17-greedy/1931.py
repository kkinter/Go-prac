import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
tasks = []
for i in range(n):
    st, en = map(int, input().split())
    tasks.append([en, st])

cnt = 0
cur = 0
for task in sorted(tasks):
    if task[1] >= cur:
        cnt += 1
        cur = task[0]

print(cnt)
# (0, 6)
# (1, 4)
# (2, 13)
# (3, 5)
# (3, 8)
# (5, 7)
# (5, 9)
# (6, 10)
# (8, 11)
# (8, 12)
# (12, 14)