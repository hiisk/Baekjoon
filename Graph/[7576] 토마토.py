from collections import deque
import sys

m, n = map(int,sys.stdin.readline().split())

queue = deque()

matrix = []
visit = [[-1]*m for _ in range(n)]

for i in range(n) :
    tmp = list(map(int, sys.stdin.readline().split()))
    matrix.append(tmp)
    for j in range(m) :
        if tmp[j] == 1 :
            queue.append([i,j])
            visit[i][j] = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(queue) :
    while queue :
        y, x = queue.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= m or ny <0 or ny >= n :
                continue
            if matrix[ny][nx] == 0 and visit[ny][nx] == -1 :
                queue.append([ny,nx])
                visit[ny][nx] = visit[y][x] + 1

    answer = 0
    for i in range(n) :
        for j in range(m) :
            if matrix[i][j] == 0 and visit[i][j] == -1 :
                return -1
            if matrix[i][j] == 0 and visit[i][j] > -1 :
                answer = max(answer,visit[i][j])
    return answer

print(bfs(queue))