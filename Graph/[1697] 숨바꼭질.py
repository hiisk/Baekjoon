import sys
from collections import deque

def dfs(start):
    deq = deque()
    deq.append(start)
    visited[start] = 1
    while deq:
        tmp = deq.popleft()
        if tmp == k:
            print(visited[tmp] - 1)
            break
        for i in (tmp-1, tmp+1, tmp*2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[tmp] + 1
                deq.append(i)

n, k = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(100001)]

dfs(n)