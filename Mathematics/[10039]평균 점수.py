answer = 0
for _ in range(5):
    tmp = int(input())
    if tmp < 40:
        tmp = 40
        answer += tmp
    else:
        answer += tmp
    
print(int(answer/5))