import sys
N, M = map(int, sys.stdin.readline().split())
dic = {}

for i in range(N):
    tmp = sys.stdin.readline().rstrip()
    dic[tmp] = i+1
    dic[str(i+1)] = tmp

for i in range(M):
    tmp = sys.stdin.readline().rstrip()
    print(dic[tmp])