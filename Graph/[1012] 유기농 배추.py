import sys
from collections import deque

T = int(sys.stdin.readline())

def bfs(graph, x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    deq = deque()
    deq.append((x,y))
    graph[x][y] = 0
    
    global count
    
    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny <0 or ny >= N:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                deq.append((nx,ny))
    return count

for _ in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    graph = [[0]*N for _ in range(M)]
    count = 0
    for i in range(K):
        X, Y = map(int,sys.stdin.readline().split())
        graph[X][Y] = 1
    for i in range(M):
        for j in range(N):
            if graph[i][j]==1:
                bfs(graph, i, j)
                count+=1
    print(count)