num = int(input())

for i in range(num):
    tmp = int(input())
    while 1:
        if tmp in (0,1):
            print(2)
            break
        check = True
        for i in range(2, int(tmp ** 0.5)+1):
            if tmp % i == 0:
                check = False
                break
        if check:
            print(tmp)
            break
        else:
            tmp+=1