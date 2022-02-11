num = int(input())

cnt = num

for i in range(num//3+1):
    for j in range(num//3-i+1):
        if num == 3*i + 5*j:
            if cnt > i+j:
                cnt = i + j
            break

if cnt == num:
    cnt = -1
    
print(cnt)