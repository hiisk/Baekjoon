import sys
N = int(input())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

result = arr[0] * N
for i in range(1, N):
    result = max(result, arr[i]*(N-i))

print(result)