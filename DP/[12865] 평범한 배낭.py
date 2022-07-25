import sys

N, K = map(int, sys.stdin.readline().split())
dp = [0] * (K+1)

for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    for j in range(K, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)
print(dp[-1])
