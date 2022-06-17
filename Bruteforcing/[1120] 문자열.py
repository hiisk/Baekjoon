A, B = input().split()

answer = len(A)

for i in range(len(B)-len(A)+1):
    tmp = 0
    for j in range(len(A)):
        if B[i+j] == A[j]:
            tmp+=1
    answer = min(answer, len(A)-tmp)
print(answer)