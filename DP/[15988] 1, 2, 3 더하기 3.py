import sys
input = sys.stdin.readline
num = int(input())
dp = [0,1,2,4,7]

for _ in range(num):
    tmp = int(input())
    for i in range(len(dp), tmp+1):
        dp.append((dp[-1]+dp[-2]+dp[-3]) % 1000000009)
    print(dp[tmp])