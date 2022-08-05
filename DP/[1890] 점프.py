N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            print(dp[i][j])
            break
        tmp = graph[i][j]
        if j + tmp < N:
            dp[i][j + tmp] += dp[i][j]
        if i + tmp < N:
            dp[i + tmp][j] += dp[i][j]