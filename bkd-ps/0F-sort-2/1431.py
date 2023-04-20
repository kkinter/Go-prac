import sys, re

sys.stdin = open("input.txt")

n = int(input())
word_list = [input() for x in range(n)]

res = sorted(word_list, key=lambda x:(len(x), sum(map(int, re.sub(r'[^0-9]', '', x))), str(x)))
for j in res:
    print(j)
