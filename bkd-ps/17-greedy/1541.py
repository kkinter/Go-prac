import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

expression = list(input())

tmp = ''
flag = False
res = 0
for e in expression:
    if '0' <= e <= '9':
        tmp += e
    else:
        if e == '+' and not flag:
            res += int(tmp)
            tmp = ''
        elif e == '-' and not flag:
            res += int(tmp)
            tmp = ''
            flag = True
        else:
            res -= int(tmp)
            tmp = ''
            flag = True

if flag:
    res -= int(tmp)
else:
    res += int(tmp)

print(res)


            
