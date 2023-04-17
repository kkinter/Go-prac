from collections import Counter

n = int(input())
for i in range(n):
    f, s = input().split()
    if Counter(f) == Counter(s):
        print("Possible")
    else:
        print("Impossible")

