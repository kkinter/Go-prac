import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
house, chicken = [], []


for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            house.append((i,j))
            
        elif row[j] == 2:
            chicken.append((i,j))


arr = []
total = float('INF')
def dfs(num,cnt):
    global total
    # num > len(chicken)의 역할은 치킨 리스트에 담은 
    # 좌표들의 개수보다 넘어가면 인덱스에러가 뜨기때문에, 그걸 잡아주는 역할
    if num > len(chicken):
        return
    
    if cnt == m:
        result_tot = 0
        for r1, c1 in house:
            dist = float('INF')
            for idx in arr:
                r2, c2 = chicken[idx]
                dist = min(dist,abs(r2-r1)+abs(c2-c1))
                
            result_tot += dist
            
        total = min(result_tot,total)
        return

    arr.append(num)
    dfs(num+1,cnt+1)
    arr.pop()
    dfs(num+1,cnt)

    return total

print(dfs(0,0))
