T = int(input())

for i in range(T):
    tmp = int(input())
    arr = [1]*tmp

    for j in range(2, tmp+1):
        for x in range(j, tmp+1, j):
            if arr[x-1] == 1:
                arr[x-1] = 0
            elif arr[x-1] == 0:
                arr[x-1] = 1
    print(sum(arr))