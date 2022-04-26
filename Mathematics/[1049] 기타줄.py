import sys

N, M = map(int, sys.stdin.readline().split())
tmp_1 = 1000
tmp_2 = 1000

for i in range(M):
    a,b = map(int, sys.stdin.readline().split())

    if tmp_1 > a:
        tmp_1 = a
    if tmp_2 > b:
        tmp_2 = b

answer = min(N//6*tmp_1 + N%6*tmp_2, (N//6+1)*tmp_1, tmp_2*N)
print(answer)