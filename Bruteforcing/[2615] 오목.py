import sys

def bfs(x, y):
    target = graph[x][y]

    for k in range(4):
        cnt = 1
        nx = x + dx[k]
        ny = y + dy[k]

        while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == target:
            cnt += 1

            if cnt == 5:
                if 0 <= x - dx[k] < 19 and 0 <= y - dy[k] < 19 and graph[x - dx[k]][y - dy[k]] == target:
                    break
                if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 and graph[nx + dx[k]][ny + dy[k]] == target:
                    break

                print(target)
                print(x + 1, y + 1)
                exit(0)

            nx += dx[k]
            ny += dy[k]

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for i in range(19):
    for j in range(19):
        if graph[i][j] != 0:
            bfs(i, j)
print(0)