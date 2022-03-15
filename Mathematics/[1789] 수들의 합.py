target = int(input())
sum = 0
tmp = 0

while True:
    tmp +=1
    sum +=tmp
    if sum > target:
        print(tmp-1)
        break
    elif sum == target:
        print(tmp)
        break