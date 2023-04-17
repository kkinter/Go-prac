import sys

sys.stdin = open("input.txt")

n = int(input())
cnt = 0

for _ in range(n):
    s = list(input())
    stk = []

    for i in range(len(s)):
        if stk:
            if s[i] == stk[-1]:
                stk.pop()
            else:
                stk.append(s[i])
        else:
            stk.append(s[i])
    if not stk:
        cnt += 1
print(cnt)
