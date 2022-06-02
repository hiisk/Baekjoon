import sys
sys.setrecursionlimit(10**6)
num, m = map(int,sys.stdin.readline().split())

check = True

graph = [[]*num for _ in range(num+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0]*(num+1)

def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)

while check:
    for i in range(1, num+1):
        if visited[i] == 0:
            dfs(i)
            cnt+=1
        if i == num:
            check = False
            break
print(cnt)