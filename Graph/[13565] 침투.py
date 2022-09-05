import sys
from collections import deque

def bfs(x, y):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    deq = deque()
    deq.append((x,y))
    graph[x][y] = 2

    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > m-1 or ny <0 or ny > n-1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                deq.append((nx,ny))

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(m)]

for i in range(n):
    if graph[0][i] == 0:
        bfs(0, i)

print("YES" if 2 in graph[-1] else "NO")