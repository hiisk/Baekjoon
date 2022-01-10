num = int(input())

answer = []

for i in range(num):
    K = int(input())
    N = int(input())
    a = list(range(1,N+1))
    for j in range(K):
        for x in range(1, N):
            a[x]+=a[x-1]
    answer.append(a[-1])

for i in range(len(answer)):
    print(answer[i])

