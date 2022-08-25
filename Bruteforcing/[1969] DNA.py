import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())

arr = [sys.stdin.readline().rstrip() for _ in range(n)]
cnt = 0

for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(arr[j][i])
    answer = sorted(Counter(tmp).most_common(), key=lambda x : (-x[1],x[0]))[0][0]
    
    for j in range(n):
        if arr[j][i] == answer:
            pass
        else:
            cnt+=1
    print(answer, end="")
print()
print(cnt)