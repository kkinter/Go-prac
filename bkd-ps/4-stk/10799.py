import sys

sys.stdin = open("input.txt")

ps = input()
ps_tmp = ps.replace('()', "*")
stk = []
res = 0
line = 0
for s in ps_tmp:
    if s == "(":
        line += 1
        res += 1
        stk.append(s)

    elif s == "*":
        res += line

    elif s == ")":
        line -= 1
        stk.pop()

print(res)