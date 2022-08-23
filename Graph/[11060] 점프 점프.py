num = int(input())
arr = list(map(int, input().split()))
dp = [num+1]*num
dp[0] = 0

for i in range(num):
    for j in range(1, arr[i]+1):
        if i+j < num:
            dp[i+j] = min(dp[i+j], dp[i]+1)
print(dp[num-1] if dp[num-1] != num+1 else -1)