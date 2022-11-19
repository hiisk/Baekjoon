N = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(arr)

for i in range(N):
    for j in range(N):
        if arr[i] == sort_arr[j]:
            arr[i] = j
            sort_arr[j] = -1
            break

print(*arr)