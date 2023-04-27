import sys
from collections import defaultdict
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
tasks = defaultdict(list)
for i in range(n):
    st, en = map(int, input().split())
    tasks[st] += [en]


cur = 0
for k, v in tasks.items():
    print(k, v)


print(tasks)