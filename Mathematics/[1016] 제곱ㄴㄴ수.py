min, max = map(int, input().split())
arr = [1 for _ in range(max-min+1)]
cnt=0
i=2
while i**2 <= max:
    tmp = min // i**2
    while tmp * (i**2) <= max:
        if tmp * (i**2) - min >= 0 and tmp * (i**2) - min <= max-min:
            arr[tmp * (i**2) - min] = 0
        tmp +=1
    i +=1

print(sum(arr))