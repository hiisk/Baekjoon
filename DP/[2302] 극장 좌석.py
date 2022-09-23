n = int(input())
m = int(input())
arr = [0]*(41)
dp = [0]*(41)
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
cnt = 0
answer = 1

for _ in range(m):
    tmp = int(input())
    arr[tmp] = 1

for i in range(1, n+1):
    if arr[i] == 0:
        cnt+=1
    elif cnt:
        answer*=dp[cnt]
        cnt = 0
if cnt:
    answer*=dp[cnt]

print(answer)