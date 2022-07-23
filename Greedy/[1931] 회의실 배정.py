n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(key = lambda x: x[0])
arr.sort(key = lambda x: x[1])

cnt = 1
target = arr[0][1]

for i in range(1, n):
    if arr[i][0] >= target:
        cnt += 1
        target = arr[i][1]

print(cnt)