import sys

sys.stdin = open("input.txt")
n = int(input())
lst = [input().split() for x in range(n)]
res = sorted(lst, key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in res:
    print(i[0])