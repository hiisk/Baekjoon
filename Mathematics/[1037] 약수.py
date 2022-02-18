num = int(input())
arr = list(map(int, input().split()))
arr.sort()

if len(arr)%2 == 0:
    print(arr[int(len(arr)/2)-1]*arr[int(len(arr)/2)])
else:
    print((arr[int(len(arr)/2)])**2)