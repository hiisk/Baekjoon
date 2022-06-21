import sys
from collections import deque

def bfs(graph, x, y, c, d):
    dx = [-2,-1,-2,-1,2,1,2,1]
    dy = [-1,-2,1,2,-1,-2,1,2]
    deq = deque()
    deq.append((x,y))
    graph[x][y] = 1
    
    while deq:
        x,y = deq.popleft()
        if x == c and y == d:
            return graph[x][y]-1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx > N-1 or ny <0 or ny > N-1:
                continue
            if graph[nx][ny] == 0:
                deq.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N = int(sys.stdin.readline().rstrip())

    graph = [[0]*N for _ in range(N)]
    
    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())
    
    if a == c and b == d:
        print(0)
        continue

    answer = bfs(graph, a, b, c, d)
    print(answer)