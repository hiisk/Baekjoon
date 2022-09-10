from collections import deque
def bfs(a,b):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    deq = deque()
    deq.append([a,b])
    graph[a][b] = "."
    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny <0 or ny >= w:
                continue

            if graph[nx][ny] == "#":
                deq.append([nx, ny])
                graph[nx][ny] = "."

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    cnt = 0 
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "#":
                bfs(i,j)
                cnt+=1
    print(cnt)
