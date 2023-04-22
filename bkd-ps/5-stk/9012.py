import sys

sys.stdin = open("input.txt")

n = int(input())
for i in range(n):
    ps = list(input())
    stk = []
    flag = True
    while ps:
        cur = ps.pop()
        if len(stk) < 1 and cur == "(":
            flag = False
            break
        elif cur == ")":    
            stk.append(cur)
        else:
            stk.pop()
    if stk:
        flag = False

    print("YES" if flag else "NO")
    




    
        