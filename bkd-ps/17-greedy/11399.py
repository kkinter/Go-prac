import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
p = sorted(list(map(int ,input().split())))
#rank = sorted([(sorted(p).index(x)+1, x) for x in p])
res = 0
for i in range(n):
    res += sum(p[:i+1])
print(res)