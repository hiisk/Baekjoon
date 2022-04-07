from math import gcd


num = int(input())
arr = list(map(int, input().split()))

for i in range(1,num):
    tmp = gcd(arr[0],arr[i])
    print(f"{arr[0]//tmp}/{arr[i]//tmp}")