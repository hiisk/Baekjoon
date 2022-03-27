import math
num = int(input())

for i in range(num):
    arr = list(map(int, input().split()))
    sum = 0
    for j in range(arr[0]-1):
        for x in range(j+1, arr[0]):
            sum += math.gcd(arr[j+1],arr[x+1])
    print(sum)