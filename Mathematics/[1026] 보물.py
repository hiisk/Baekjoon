N = int(input())

answer = 0
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(N):
    answer +=(A[i] * B[i])
print(answer)