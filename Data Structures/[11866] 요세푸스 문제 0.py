import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

deq = deque(list(range(1, N+1)))
tmp = 0
answer = []
while deq:
    if tmp < K-1:
        tmp+=1
        deq.rotate(-1)
    else:
        answer.append(str(deq[0]))
        deq.popleft()
        tmp = 0
print("<",", ".join(answer)[:],">", sep='')
