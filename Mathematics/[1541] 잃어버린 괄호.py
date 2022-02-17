num = input().split('-')
arr = []
for i in num:
    tmp = 0
    s = i.split('+')
    for j in s:
        tmp += int(j)
    arr.append(tmp)
n = arr[0]

for i in range(1, len(arr)):
    n -= arr[i]
print(n)