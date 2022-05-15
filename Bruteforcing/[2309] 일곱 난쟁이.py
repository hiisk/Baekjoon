import sys
from itertools import combinations

input = sys.stdin.readline
arr = []

for i in range(9):
    tmp = int(input())
    arr.append(tmp)
arr.sort()

answer = list(combinations(arr,7))

for i in answer:
    if sum(i) == 100:
        i = list(i)
        print('\n'.join(map(str, i)))
        break