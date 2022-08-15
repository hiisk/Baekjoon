num = int(input())
    
while 1:
    if num ==1:
        print(2)
        break

    if str(num) == str(num)[::-1]:
        pass
    else:
        num+=1
        continue

    check = True
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            check = False
            break

    if check:
        print(num)
        break
    else:
        num+=1