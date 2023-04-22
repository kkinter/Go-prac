import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def lotto(depth, k, m):
    if depth == m:
        print(*tmp)
        return
    prev = -1
    for i in range(k):
        if prev != nlist[i]:
            if not tmp or tmp[-1] < nlist[i]:
                tmp.append(nlist[i])
                lotto(depth+1, k, m)
                tmp.pop()

while True:
    case = list(map(int, input().split()))
    if len(case) == 1:
        break
    k, *nlist = case
    tmp = []

    lotto(0, k, 6)
    print()

    
    
 
    