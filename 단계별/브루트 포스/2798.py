N, M = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0
diff = M

for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for x in range(j+1, len(arr)):
            if M - (arr[i] + arr[j] + arr[x]) < diff and (arr[i] + arr[j] + arr[x]) <= M:
                answer = arr[i] + arr[j] + arr[x]
                diff = M - (arr[i] + arr[j] + arr[x])
            else:
                continue
print(answer)