n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

for i in range(n):
    arr[i] = arr[i]+2+i

print(max(arr))
