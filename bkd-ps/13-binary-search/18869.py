import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 우주의 개수 m, 우주에 있는 행성의 개수 n

def search(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        
        if arr[mid] > target:
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            return mid
    return

m, n = map(int, (input().split()))
universe = []
for _ in range(m):
    planet = list(map(int, input().split()))
    tmp = sorted(set(planet))
    res = [0] * n
    for i in range(n):
        res[i] = search(tmp, planet[i])
    universe.append(res)

cnt = 0
unique = set()
duple = set()

for sublist in universe:
    tuple_sublist = tuple(sublist)
    if tuple_sublist in unique:
        duple.add(tuple_sublist)
    else:
        unique.add(tuple_sublist)

print(len(duple))
