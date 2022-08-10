arr = list(map(int,input().split()))
cnt = 0
num = 1

while cnt < 3:
    cnt = 0
    for i in arr:
        if num % i == 0 :
            cnt += 1
        if cnt == 3:
            break
    num += 1
print(num-1)