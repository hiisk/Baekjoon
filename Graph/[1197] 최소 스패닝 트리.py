from heapq import heappush, heappop
import sys
input=sys.stdin.readline

def prim(start, weight) :
    visited=[0]*(V+1)
    queue=[[weight, start]]
    answer=0
    cnt=0
    while cnt < V :
        k, v=heappop(queue)
        if visited[v] : continue
        visited[v]=1
        answer+=k
        cnt+=1
        for u, w in G[v] :
            heappush(queue, [w, u])
    return answer

V, E=map(int, input().split())
G=[[] for _ in range(V+1)]
for _ in range(E) :
    u, v, w=map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

print(prim(1, 0))