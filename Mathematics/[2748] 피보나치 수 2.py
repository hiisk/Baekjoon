num = int(input())
arr = [0]*(num+1)
arr[0] = 0
arr[1] = 1

if num >1:
    for i in range(2, num+1):
        arr[i] = arr[i-1] + arr[i-2]

print(arr[num])
