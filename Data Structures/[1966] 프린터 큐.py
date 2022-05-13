import sys
from collections import deque

num = int(sys.stdin.readline())

for i in range(num):
    n, m = map(int, sys.stdin.readline().split())
    deq = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0

    while deq:
        target = max(deq)  
        front = deq.popleft()
        m -= 1

        if target == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break

        else: 
            deq.append(front)
            if m < 0 :
                m = len(deq) - 1
