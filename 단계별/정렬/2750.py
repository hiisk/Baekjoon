num = int(input())

arr = []

for _ in range(num):
    arr.append(int(input()))
    
answer = sorted(arr)

for i in range(num):
    print(answer[i])