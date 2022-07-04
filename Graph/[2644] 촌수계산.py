n = int(input())
graph = [[] for i in range(n+1)]
start, dest = map(int, input().split())
m = int(input())
visited = [False]*(n+1)
cnt = [0]*(n+1)

def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            cnt[i] = cnt[x]+1
            dfs(i)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(start)
if cnt[dest] > 0:
    print(cnt[dest])
else:
    print(-1)
