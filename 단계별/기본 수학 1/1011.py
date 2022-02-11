num = int(input())
answer = []


for i in range(num):
    x,y = map(int, input().split())
    cnt = 1
    target = y - x
    tmp = 0
    count = 0
    for j in range(target):
        if tmp < target-cnt:
            tmp += cnt
            count +=1
            if tmp < target-cnt:
                tmp += cnt
                count +=1
            cnt += 1
            if tmp >= target:
                answer.append(count)
                break

        else:
            count +=1
            answer.append(count)
            break

for i in range(len(answer)):
    print(answer[i])