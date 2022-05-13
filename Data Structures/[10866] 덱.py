from collections import deque
import sys

num = int(sys.stdin.readline())
deq = deque()

for i in range(num):
    tmp = list(sys.stdin.readline().split())
    if tmp[0] =="push_front":
        deq.appendleft(tmp[1])
    elif tmp[0] =="push_back":
        deq.append(tmp[1])
    elif tmp[0] =="pop_front":
        if len(deq) > 0:
            print(deq.popleft())
        else:
            print(-1)
    elif tmp[0] =="pop_back":
        if len(deq) > 0:
            print(deq.pop())
        else:
            print(-1)
    elif tmp[0] =="size":
        print(len(deq))
    elif tmp[0] =="empty":
        if len(deq) > 0:
            print(0)
        else:
            print(1)
    elif tmp[0] =="front":
        if len(deq) > 0:
            print(deq[0])
        else:
            print(-1)
    elif tmp[0] =="back":
        if len(deq) > 0:
            print(deq[-1])
        else:
            print(-1)