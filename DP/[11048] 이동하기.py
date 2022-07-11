import sys
n, m = map(int,sys.stdin.readline().rstrip().split())

graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = graph[0][0]

for i in range(n):
    for j in range(m):
        x = i+1
        y = j+1
        if x < n and y < m:
            dp[x][y] = max(dp[i][j]+graph[x][y], dp[x][y])
        if x <= n and y < m:    
            dp[i][y] = max(dp[i][j]+graph[i][y], dp[i][y])
        if x < n and y <= m:    
            dp[x][j] = max(dp[i][j]+graph[x][j], dp[x][j])

print(dp[n-1][m-1])