import sys
from collections import deque
input = sys.stdin.readline
    
n, m = map(int, input().split())    
arr = [list(map(int, ' '.join(input()).split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

deq = deque([(0, 0)])
result = 0

while deq:
    x, y = deq.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                deq.append((nx, ny))
                
print(arr[n-1][m-1])