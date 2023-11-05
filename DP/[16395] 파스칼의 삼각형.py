n, k = map(int, input().split())
arr = []

for i in range(n):
    arr.append([1]*(i+1))

for i in range(1,n):
    for j in range(1,i):
        arr[i][j] = arr[i-1][j]+ arr[i-1][j-1]
print(arr[n-1][k-1])