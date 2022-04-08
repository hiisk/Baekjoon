num = int(input())
tmp = num
answer = 0

n_1 = 9
if num<10:
    answer = num
else:
    for i in range(len(str(num))-1):
        if i ==0:
            answer += (10**i*n_1)
        else:
            answer += (10**i*n_1)*(i+1)
    answer+=(tmp-int(str(9)*(len(str(num))-1)))*len(str(num))
print(answer)
