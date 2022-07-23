from collections import deque
import sys

def bfs(x):
    deq = deque([x])
    visited[x] = 1
    global cnt
    while deq:
        tmp = deq.popleft()
        for i in graph[tmp]:
            if visited[i] == 0:
                visited[i] = 1
                deq.append(i)
                cnt+=1

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[]*(n+1) for _ in range(n+1)]
answer = [0]*(n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[b].append(a)

for i in range(1, n+1):
    visited = [0]*(n+1)
    if graph[i]:
        cnt = 0
        bfs(i)
        answer[i] = cnt

max_value = max(answer)

for i in range(len(answer)):
    if answer[i] == max_value:
        print(i, end=" ")