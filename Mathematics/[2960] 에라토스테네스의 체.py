n, k = map(int, input().split())

arr = list(range(2,n+1))
answer = []

for tmp in range(2,n+1):
    for i in arr:
        if i%tmp == 0 and i not in answer:
            answer.append(i)
print(answer[k-1])