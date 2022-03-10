sum = 0
min = 101

for i in range(7):
    tmp = int(input())
    if tmp %2 != 0:
        sum += tmp
        if tmp < min:
            min = tmp
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)