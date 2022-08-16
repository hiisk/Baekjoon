num = int(input())
arr = list(map(int, input().split()))
cnt = 0
dp = [1]*num

for i in range(1, num):
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))