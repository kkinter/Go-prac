import sys
import re
sys.stdin = open("input.txt")

s = input().replace('()', '2').replace('[]', '3')
print(s)