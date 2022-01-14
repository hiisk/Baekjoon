num = int(input())
target = list(map(int, input().split()))
cnt = 0

for i in range(num):
    if target[i] == 1:
        continue
    elif target[i] == 2:
        cnt +=1
    else:
        tmp = 1
        while True:
            tmp +=1
            if target[i]/tmp == target[i]//tmp and target[i] != tmp:
                break
            elif target[i] == tmp:
                cnt +=1
                break

print(cnt)