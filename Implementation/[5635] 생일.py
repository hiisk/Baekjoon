n = int(input())
arr = []
for _ in range(n):
    tmp = list(input().split())
    for i in range(1,4):
        tmp[i] = int(tmp[i])
    arr.append(tmp)
arr.sort(key = lambda x: (x[3], x[2], [1]))
print(arr[-1][0])
print(arr[0][0])