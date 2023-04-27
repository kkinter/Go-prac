import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))
rank = sorted([(sorted(aList).index(x), x) for x in aList])

res = 0
for r, v in rank:
    tmp = max(bList)
    res += v * tmp
    bList.remove(tmp)
print(res)
