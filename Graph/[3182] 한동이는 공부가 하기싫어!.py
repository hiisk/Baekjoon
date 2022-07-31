from collections import deque

def bfs(x):
    deq = deque()
    deq.append(x)
    global cnt
    visited[x] = True
    while deq:
        tmp = deq.popleft()
        for i in graph[tmp]:
            if not visited[i]:
                deq.append(i)
                visited[tmp] = True
                cnt+=1
    return cnt

n = int(input())
graph = [[] for _ in range(n+1)]
value = 0
answer = 0
for i in range(n):
    graph[i+1].append(int(input()))

for i in range(1, n+1):
    cnt = 1
    visited = [False]*(n+1)
    bfs(i)
    if value < cnt:
        value = cnt
        answer = i
print(answer)