fl = list(input())
sl = list(input())
cnt = 0
d = len(fl) + len(sl)

for i in sl:
    if i in fl:
        fl.remove(i)
        d -= 2

print(d)