import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, c = map(int, input().split())
homelist = sorted([int(input()) for x in range(n)])
print(homelist)
ans = float("-INF")
