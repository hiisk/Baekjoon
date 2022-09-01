while 1:
    try:
        num = int(input())
    except:
        break

    target = 0
    answer = 1
    while 1:
        target = target * 10 + 1
        target %= num
        if target == 0:
            print(answer)
            break
        answer +=1