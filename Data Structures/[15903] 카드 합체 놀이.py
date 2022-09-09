n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in range(m):
    tmp = arr[0] + arr[1]
    arr[0] = tmp
    arr[1] = tmp
    arr.sort()
print(sum(arr))
