import sys
from collections import deque

def bfs(deq):
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]

    while deq:
        x,y = deq.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny <0 or ny >= M:
                continue

            if graph[nx][ny] == 0:
                deq.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

N, M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
count = 0
deq = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            deq.append((i,j))
bfs(deq)

ans = 0
for i in range(N):
    tmp = max(graph[i])
    if ans < tmp:
        ans = tmp
print(ans-1)