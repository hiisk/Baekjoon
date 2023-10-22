tmp = list(input())
cnt = 0

while 1:
    result = 0
    cnt+=1
    for i in tmp:
        result += int(i)
    if len(tmp) == 1:
        cnt -=1
    if result < 10:
        print(cnt)
        if result%3 == 0:
            print("YES")
            break
        else:
            print("NO")
            break
    tmp = list(str(result))
