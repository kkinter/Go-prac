import sys
import collections
import pprint

sys.stdin = open('input.txt', "r")

n = int(input())
# node_list = collections.defaultdict(list)
# for i in range(n - 1):
#     v, w = map(int, input().split())
#     node_list[v].append(w)
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)






"""
{
    1: [6], 
    6: [3], 
    3: [5], 
    4: [1, 7], 
    2: [4]
}
"""
