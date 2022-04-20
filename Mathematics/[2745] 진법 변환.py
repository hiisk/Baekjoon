b, n = input().split()

n = int(n)
tmp = 0
answer = 0

for i in b[::-1]:
    if i.isnumeric():
        num = int(i)       
    else:
        num = ord(i)-55

    if tmp == 0:
        answer += (num)
    else:
        answer += (num)*(n**tmp)
    tmp +=1
print(answer)
