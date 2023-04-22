import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))
c = combinations(solutions, 2)
sum_dict = {x:abs(sum(x)) for x in c}

print(sum_dict)
