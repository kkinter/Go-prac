s = input()
arr = [0] * 10
tmp = [0, 0]
res = 0
for i in s:
    if int(i) == 6 or int(i) == 9:
        tmp[int(i)//7] += 1
    else:
        arr[int(i)] += 1
        res = max(res, arr[int(i)])

if sum(tmp) % 2 == 0:
    res = max(res, sum(tmp) // 2)
else:
    res = max(res, sum(tmp) // 2 + 1)


print(res)