import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [sys.stdin.readline().rstrip() for _ in range(n)]

answer = 1

for i in range(n):
    for j in range(m):
        for k in range(answer,50):
            if n<=i+k or m<=j+k:
                break
            if len(set([graph[i][j],graph[i+k][j],graph[i][j+k],graph[i+k][j+k]])) == 1:
                answer = max(answer,k+1)
print(answer**2)