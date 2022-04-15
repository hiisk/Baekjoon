num = int(input())
arr = list(map(int, input().split()))
answer = 0
tmp = 1

if arr[0] == 1:
    answer +=1

for i in range(1, num):
    if arr[i] == 1 and arr[i-1] == 1:
        tmp +=1
        answer += tmp
    elif arr[i] ==1 and arr[i-1] == 0:
        tmp = 1
        answer += tmp
    else:
        tmp = 0
print(answer)