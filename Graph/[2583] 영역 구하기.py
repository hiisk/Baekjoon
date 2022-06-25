import sys
sys.setrecursionlimit(100000)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<M and -1<ny<N and graph[nx][ny] == 0:
            graph[nx][ny] = 1
            cnt += 1
            dfs(nx,ny)

M, N, K = map(int, sys.stdin.readline().split())
graph = [[0]*N for _ in range(M)]
answer = []

for i in range(K):
    x_1, y_1 ,x_2, y_2 = map(int, sys.stdin.readline().split())
    for x in range(y_1, y_2):
        for y in range(x_1, x_2):
            graph[x][y] = 1

for x in range(M):
    for y in range(N):
        cnt = 0
        if graph[x][y] == 0:
            cnt += 1
            graph[x][y] = 1
            dfs(x,y)
            answer.append(cnt)

print(len(answer))
print(*sorted(answer))