import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

m, n = map(int, input().split())
universe = defaultdict(int)

for _ in range(m):
    planets = list(map(int, input().split()))
    sortedPlanets = sorted(list(set(planets)))
    rank = {sortedPlanets[i] : i for i in range(len(sortedPlanets))}
    vector = tuple([rank[i] for i in planets])
    universe[vector] += 1
    print(vector)

sum = 0

for i in universe.values():
    sum += (i * (i - 1)) // 2 # nC2
print(sum)
