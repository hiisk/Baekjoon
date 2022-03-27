arr = list(map(int, input().split()))

answer = [1, 1, 2, 2, 2, 8]
for i in range(len(arr)):
    answer[i] -= arr[i]

print(" ".join(map(str,answer)))