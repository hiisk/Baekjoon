from collections import deque
import sys
N = int(sys.stdin.readline())
deq = deque()

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))

    if tmp[0] == 1:
        deq.appendleft(tmp[1])
    elif tmp[0] == 2:
        deq.append(tmp[1])
    elif tmp[0] == 3:
        print(deq.popleft() if (deq) else -1)
    elif tmp[0] == 4:
        print(deq.pop() if (deq) else -1)
    elif tmp[0] == 5:
        print(len(deq))
    elif tmp[0] == 6:
        print(0 if (deq) else 1)
    elif tmp[0] == 7:
        print(deq[0] if (deq) else -1)
    elif tmp[0] == 8:
        print(deq[-1] if (deq) else -1)