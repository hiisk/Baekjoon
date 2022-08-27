num = int(input())
answer = 0
arr = [int(input()) for _ in range(num)]

for i in range(num-2, -1, -1):
    if arr[i] >= arr[i+1]:
        answer += arr[i] - arr[i+1] +1
        arr[i] = arr[i+1]-1
print(answer)