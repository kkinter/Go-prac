import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
students = sorted(list(map(int, input().split())))
print(students)

ans = float("INF")
ans_left = 0
ans_right = 0
l = 0
r = n - 1
while l <= r:
    cur = students[l] + students[r]
    mid = (l + r) // 2
    
    if abs(cur + mid) <= abs:
