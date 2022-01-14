num = int(input())
target = int(input())
cnt = 0
min = 0

for i in range(num, target+1):
    if i == 1:
        continue
    else:
        tmp = 1
        while True:
            tmp +=1
            if i/tmp == i//tmp and i != tmp:
                break
            elif i == tmp:
                cnt +=tmp
                if min == 0:
                    min = tmp
                break
if cnt == 0:
    print(-1)
else:
    print(cnt)
    print(min)