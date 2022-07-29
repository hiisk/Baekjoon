import sys
from collections import deque

def bfs(x):
    deq = deque([x])
    cnt = 0
    for _ in range(n):
        target = deq.popleft()
        cnt += 1

        if graph[target] == k:
            return cnt

        deq.append(graph[target])
    return -1

n, k = map(int, sys.stdin.readline().split())
graph = [int(sys.stdin.readline()) for _ in range(n)]

print(bfs(0))