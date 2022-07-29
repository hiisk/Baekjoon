from collections import deque

def bfs(a, b):
    deq = deque([(a,b)])
    while deq:
        x, y = deq.popleft()
        if graph[x][y] == "-":
            graph[x][y] = "1"
            if y+1 < m and graph[x][y+1] == "-":
                deq.append((x,y+1))
        elif graph[x][y] == "|":
            graph[x][y] = "1"
            if x+1 < n and graph[x+1][y] == "|":
                deq.append((x+1,y))

n, m = map(int,input().split())
cnt = 0
graph = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] != "1":
            bfs(i,j)
            cnt+=1
print(cnt)