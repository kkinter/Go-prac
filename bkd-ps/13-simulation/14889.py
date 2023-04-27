import sys
from collections import deque
from itertools import combinations
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
team = [list(map(int, input().split())) for _ in range(n)]
comb = list(combinations([x for x in range(1, n+1)], n//2))
res = []
for i in range(len(comb)//2):
    st = comb[i]
    li= comb[len(comb)-1-i]

s = 0
e = len(comb)-1
res = float('INF')
while s < e:
    st = comb[s]
    li = comb[e]

    stsum = 0
    lisum = 0
    for i in combinations(st, 2):
        stsum += team[i[0]-1][i[1]-1]+ team[i[1]-1][i[0]-1]
        
    for j in combinations(li, 2):
        lisum += team[j[0]-1][j[1]-1]+ team[j[1]-1][j[0]-1]
    
    res = min(abs(stsum-lisum), res)
    
    s+=1
    e-=1

print(res)