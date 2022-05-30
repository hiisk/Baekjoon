import sys
num = int(sys.stdin.readline())
arr = []

for i in range(num):
    tmp = list(map(int,sys.stdin.readline().split()))
    if len(arr)==0:
        arr = tmp
    else:
        tmp[0] = tmp[0] + arr[0]
        tmp[len(arr)] = tmp[len(arr)] + arr[len(arr)-1]
        
        for j in range(1, len(arr)):
            tmp[j] = max(tmp[j]+arr[j-1], tmp[j]+arr[j])
        arr = tmp

print(max(arr))