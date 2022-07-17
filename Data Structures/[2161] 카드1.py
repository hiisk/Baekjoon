from collections import deque

deq = deque([i for i in range(1, int(input())+1)])

while deq:
    print(deq.popleft(), end=" ")
    deq.rotate(-1)