import sys

def dfs(i, graph, n):
    visit = [0] * n
    q = [i]

    while q:
        tmp = q.pop(0)
        for i, v in enumerate(graph[tmp]):
            if visit[i] == 0 and v == 1:
                visit[i] = 1
                q.append(i)

    return visit

n = int(sys.stdin.readline().rstrip())
graph = []

for _ in range(n):
    graph.append([*map(int,sys.stdin.readline().rstrip().split())])

for i in range(n):
    print(' '.join(map(str,dfs(i,graph,n))))