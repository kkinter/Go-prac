import sys
from collections import defaultdict

sys.stdin = open("input.txt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(node, graph, parent):
    for adjacent_node in graph[node]:
        # 방문하지 않은 노드인 경우
        if parent[adjacent_node] == 0:
            # 부모로 설정한다
            parent[adjacent_node] = node
            dfs(adjacent_node, graph, parent)


n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n + 1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, graph, parent)

for i in range(2, n+1):
    print(parent[i])
