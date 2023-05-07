import sys
from collections import defaultdict
sys.stdin = open("input.txt")
input = sys.stdin.readline

groupMap = defaultdict(list)

n, m = map(int, input().split())
for i in range(n):
    group = input().strip('\n')
    numbers = int(input())
    for num in range(numbers):
        name = input().strip('\n')
        groupMap[group].append(name)

for j in range(m):
    name = input().strip('\n')
    quiz = int(input())

    if quiz == 1:
        for i, (group, members) in enumerate(groupMap.items()):
            if name in members:
                print(group)
    else:
        for i, (group, members) in enumerate(groupMap.items()):
            if name == group:
                print(*sorted(members), sep='\n')
