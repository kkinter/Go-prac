n = int(input())
res = []

for i in range(n):
    res.append(int(input()))
res = sorted(res, reverse=True)
for j in res:
    print(j)