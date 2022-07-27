from collections import deque

def bfs():
    deq = deque()
    deq.append((0,0))
    while deq:
        x,y = deq.popleft()
        if graph[x][y] == 0:
            continue
        if graph[x][y] == -1:
            return "HaruHaru"
        if x+graph[x][y] < n:
            deq.append((x+graph[x][y],y))
        if y+graph[x][y] < n:
            deq.append((x,y+graph[x][y]))
    return "Hing"

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
print(bfs())