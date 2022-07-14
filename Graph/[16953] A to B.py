from collections import deque

a,b = map(int,input().split())
deq = deque()
deq.append((a,1))

while deq:
    n, cnt = deq.popleft()
    if n > b:
        continue
    if n == b:
        print(cnt)
        break
    deq.append((int(str(n)+"1"), cnt+1))
    deq.append((n*2, cnt+1))
else:
    print(-1)