import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
n, c = map(int, input().split())
sequence = list(map(int, input().split()))
q = sorted(sequence, key=lambda x:(-(sequence.count(x)), sequence.index(x)))
print(*q)