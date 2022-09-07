num = int(input())

arr = [0] + list(map(int,input().split()))
dp = [0] +[int(num/i*arr[i]) for i in range(1, num+1)]

for i in range(1,num+1):
    for k in range(1,i+1):
        dp[i] = min(dp[i], dp[i-k] + arr[k])

print(dp[num])