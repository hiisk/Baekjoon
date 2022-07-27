from collections import deque

def bfs():
    deq = deque()
    deq.append(1)
    global cnt
    visited = [False]*(n+1)
    visited[1] = True
    while deq:
        x = deq.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                deq.append(i)
                cnt+=1
    return cnt

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    cnt = 0
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(bfs())

import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
    print(n-1)