from collections import deque
import copy
def bfs(a,b):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    deq = deque()
    deq.append([a,b])
    tmp = graph[a][b]
    graph[a][b] = "."
    global cnt

    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny <0 or ny >= N:
                continue

            if graph[nx][ny] == tmp:
                deq.append([nx, ny])
                graph[nx][ny] = "."
    cnt+=1

def bfs_2(a,b):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    deq = deque()
    deq.append([a,b])
    tmp_2 = graph_2[a][b]
    graph_2[a][b] = "."
    global cnt_2

    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny <0 or ny >= N:
                continue
            
            if (graph_2[nx][ny] == "R" or graph_2[nx][ny] == "G") and tmp_2 in ("R","G"):
                    deq.append([nx, ny])
                    graph_2[nx][ny] = "."
            elif graph_2[nx][ny] == "B" and tmp_2 == "B":
                    deq.append([nx, ny])
                    graph_2[nx][ny] = "."
    cnt_2+=1

N = int(input())
graph = [list(input()) for _ in range(N)]
cnt = 0
cnt_2 = 0
graph_2 = copy.deepcopy(graph)

for i in range(N):
    for j in range(N):
        if graph[i][j] != ".":
            bfs(i,j)
        if graph_2[i][j] != ".":
            bfs_2(i,j)

print(cnt, cnt_2)