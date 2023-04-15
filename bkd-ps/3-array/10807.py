n = int(input())
a = [0]*201

for i in map(int, input().split()):
    a[i + 100] += 1

v = int(input())
print(str(a[v+100]))
