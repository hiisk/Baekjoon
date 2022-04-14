N, M = map(int, input().split())
tmp_1 = []

for _ in range(N):
    tmp_1.append(list(map(int, input().split())))

M, K = map(int, input().split())
tmp_2 = []

for _ in range(M):
    tmp_2.append(list(map(int, input().split())))

answer = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            answer[n][k] += tmp_1[n][m] * tmp_2[m][k]


for i in answer:
    for j in i:
        print(j, end = ' ')
    print()