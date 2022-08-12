from collections import deque
n, l = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
deq = deque(arr)

tmp = deq.popleft()
cnt = 1
while deq:
    x = deq.popleft()
    if x < tmp+l:
        continue
    else:
        tmp = x
        cnt+=1
print(cnt)