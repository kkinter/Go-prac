def check(x):
    total = 0

    for i in li:
        total += i // x
    return total >= n

n, m = map(int, input().split())
li = list(map(int, input().split()))

s = 0
e = float("inf")


while s <= e:
    if (s + e) == 0:
        print(0)
        exit()

    mid = (s + e) // 2
    if check(mid):
        ans = mid
        s = mid + 1
    else:
        e = mid - 1