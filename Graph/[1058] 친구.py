from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
friends = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    tmp = list(input().rstrip())
    for j in range(n):
        if tmp[j] == 'Y':
            friends[i][j] = 1

def bfs(n, i):
    visited = [0] * n
    visited[i] = 1
    deq = deque([(i, 0)])
    count = 0
    while deq:
        j, cnt = deq.popleft()
        if cnt >= 2:
            continue
            
        for k in range(n):
            if not visited[k] and friends[j][k]:
                count += 1
                visited[k] = 1
                deq.append((k, cnt+1))
                
    return count
        
answer = 0
for i in range(n):
    answer = max(answer, bfs(n, i))
print(answer)