import sys
a, b = map(int, sys.stdin.readline().split())
n = {sys.stdin.readline().rstrip() for _ in range(a)}
cnt = 0

for i in range(b):
    if sys.stdin.readline().rstrip() in n:
        cnt+=1
print(cnt)
