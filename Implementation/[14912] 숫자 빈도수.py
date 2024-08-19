import sys
n, d = map(int, sys.stdin.readline().split())
cnt = 0

for i in range(1, n+1):
    if str(i).count(str(d)) > 0:
        if i > 9:
            cnt += list(str(i)).count(str(d))
        else:
            cnt += 1

print(cnt)