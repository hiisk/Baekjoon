from collections import deque
num = int(input())

deq = deque(enumerate(map(int, input().split()), start=1))

while deq:
    tmp = deq.popleft()
    print(tmp[0], end=' ')
    if tmp[1] > 0:
        deq.rotate(-(tmp[1] - 1))
    else:
        deq.rotate(-tmp[1])