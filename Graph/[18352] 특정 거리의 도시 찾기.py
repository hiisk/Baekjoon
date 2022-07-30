import sys
from collections import deque

def dfs(x, k):
    deq = deque()
    deq.append(x)
    visited[x] = 0
    while deq:
        tmp = deq.popleft()
        for i in graph[tmp]:
            if i != x and visited[i] == 0 and k > visited[tmp]:
                visited[i] = visited[tmp] + 1
                deq.append(i)

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
answer = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

dfs(x, k)

for i in range(n+1):
    if visited[i] == k:
        answer.append(i)
if answer:
    print(*answer, sep="\n")
else:
    print(-1)