import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

cards = deque([x for x in range(1, int(input()) + 1)])
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(*cards)