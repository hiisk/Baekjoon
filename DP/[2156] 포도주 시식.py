import sys

n = int(sys.stdin.readline())
arr = [0 for _ in range(10000)]
dp = [0 for _ in range(10000)]

for i in range(n):
    arr[i] = int(sys.stdin.readline())

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[1] + arr[2], arr[0] + arr[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1])

print(max(dp))