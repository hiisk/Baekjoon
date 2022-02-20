N = int(input())
tmp = 1
answer= 0

if N < 5:
    print(answer)
else:
    for i in range(2, N+1):
        tmp*=i
    tmp = str(tmp)

    for i in tmp[::-1]:
        if int(i) == 0:
            answer +=1
        else:
            print(answer)
            break
