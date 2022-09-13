import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = [*map(int, input().split())]

answer = [arr[0]]

for i in arr:
    if answer[-1] < i:
        answer.append(i)
    else:
        idx = bisect_left(answer, i)
        answer[idx] = i
print(len(answer))