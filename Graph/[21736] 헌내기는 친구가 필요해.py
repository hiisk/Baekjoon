import sys
from collections import deque

def bfs(x, y):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    deq = deque()
    deq.append((x,y))
    graph[x][y] = "X"
    global answer

    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny <0 or ny > m-1:
                continue
            if graph[nx][ny] == "O":
                graph[nx][ny] = "X"
                deq.append((nx,ny))
            elif graph[nx][ny] == "P":
                graph[nx][ny] = "X"
                deq.append((nx,ny))
                answer+=1

n, m = map(int, sys.stdin.readline().split())
graph = [list(list(sys.stdin.readline().rstrip())) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            bfs(i,j)
if answer:
    print(answer)
else:
    print("TT")