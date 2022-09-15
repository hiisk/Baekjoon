from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(graph,x,y):

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    deq = deque()
    deq.append((x,y))
    graph[x][y] = 0
    cnt = 1

    while deq:
        x,y = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                deq.append((nx,ny))
                cnt += 1
    return cnt

count = [bfs(graph, i, j) for i in range(n) for j in range(m) if graph[i][j] == 1]

print(len(count))
if count:
    print(max(count))
else:
    print(0)