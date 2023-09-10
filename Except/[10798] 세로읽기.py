arr = []
answer = ''
max_length = 0
for _ in range(5):
    tmp = list(input())
    arr.append(tmp)
    max_length = max(max_length,len(tmp))

for i in range(max_length):
    for j in range(5):
        if i < len(arr[j]):
            answer = answer + arr[j][i]

print(answer)