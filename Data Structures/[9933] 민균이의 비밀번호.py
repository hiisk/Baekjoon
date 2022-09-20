num = int(input())
arr = [input() for _ in range(num)]
for i in range(num):
    if arr[i] == arr[i][::-1]:
        print(len(arr[i]), arr[i][len(arr[i])//2])
        exit()

arr.sort(key = lambda x:len(x))
for i in range(num-1):
    for j in range(i+1, num):
        if arr[i] == arr[j][::-1]:
            print(len(arr[i]), arr[i][len(arr[i])//2])
            exit()
        elif len(arr[i]) != len(arr[j]):
            continue