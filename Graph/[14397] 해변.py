import sys
n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == "#":
            if i % 2 == 0:
                dx = [1,-1, 0, 0, -1, 1]
                dy = [0, 0 , 1, -1, -1, -1]
                for x in range(6):
                    a = i + dx[x]
                    b = j + dy[x]
                    if a < 0 or a > n-1 or b < 0 or b > m-1:
                        continue
                    if graph[a][b] == ".":
                        cnt+=1
            else:
                dx = [1,-1, 0, 0, 1, -1]
                dy = [0, 0 , 1, -1, 1, 1]
                for x in range(6):
                    a = i + dx[x]
                    b = j + dy[x]
                    if a < 0 or a > n-1 or b < 0 or b > m-1:
                        continue
                    if graph[a][b] == ".":
                        cnt+=1                
print(cnt)
