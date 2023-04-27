import sys
from collections import deque
from itertools import combinations, permutations
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

maxval = float("-INF")
minval = float("INF")

def solve(depth, total, plus, minus, multiply, divide):
    global maxval, minval
    if depth == n:
        maxval = max(total, maxval)
        minval = min(total, minval)
        return
    
    if plus:
        solve(depth+1, total + nums[depth], plus-1, minus, multiply, divide)
    
    if minus:
        solve(depth+1, total - nums[depth], plus, minus-1, multiply, divide)
    
    if multiply:
        solve(depth+1, total * nums[depth], plus, minus, multiply-1, divide)
    
    if divide:
        solve(depth+1, int(total / nums[depth]), plus, minus, multiply, divide-1)

solve(1, nums[0], op[0], op[1], op[2], op[3])
print(maxval)
print(minval)