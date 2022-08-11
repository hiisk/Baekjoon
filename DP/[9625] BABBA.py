k = int(input())

dp = [[0, 1]] *k

for i in range(1, k):
    dp[i] = [dp[i-1][1], dp[i-1][1]+dp[i-1][0]]
print(*dp[-1])