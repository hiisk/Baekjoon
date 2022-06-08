import sys
from collections import deque

def bfs(graph, x, y):
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]
    deq = deque()
    deq.append((x,y))
    graph[x][y] = 0
    
    global count
    
    while deq:
        x,y = deq.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > N-1 or ny <0 or ny > M-1:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                deq.append((nx,ny))
    return count

while 1:
    M, N = map(int,sys.stdin.readline().split())
    if M == 0 and N == 0:
        break

    graph = []
    count = 0

    for i in range(N):
        graph.append(list(map(int,sys.stdin.readline().split())))
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1:
                bfs(graph, i, j)
                count+=1
    print(count)