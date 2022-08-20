import sys
from itertools import combinations

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

com = []
for i in range(1, N+1):
    com.append(combinations(arr, i))

answer = 1000000000
for i in com:
    for j in i:
        x = 1
        y = 0
        for z in j:
            x *= z[0]
            y += z[1]
        answer = min(answer, abs(x - y))

print(answer)