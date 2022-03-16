M = int(input())
N = int(input())
min = 10001
sum = 0

arr = list(range(1,101))
for i in range(len(arr)):
    arr[i] = arr[i]**2

for i in arr:
    if M <= i and i<= N:
        sum +=i
        if min == 10001:
            min = i
    elif i>N:
        break

if sum >0:
    print(sum)
    print(min)
else:
    print(-1)
