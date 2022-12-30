import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0]*n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i < 2:
        print(dp[j-1])
    else:
        print(dp[j-1]-dp[i-2])