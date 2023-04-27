import sys
from heapq import heappop, heappush
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heap = []
for card in cards:
    heappush(heap, card)

while m > 0:
    x = heappop(heap)
    y = heappop(heap)
    heappush(heap, x+y)
    heappush(heap, x+y)
    m -= 1
print(heap)
