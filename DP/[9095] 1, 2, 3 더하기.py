import sys
input = sys.stdin.readline

def dp(n):
    if n == 1 or n ==2:
        return n
    elif n ==3 :
        return 4
    else:
        return dp(n-1) + dp(n-2) +dp(n-3)

num = int(input())
for _ in range(num):
    tmp = int(input())
    print(dp(tmp))