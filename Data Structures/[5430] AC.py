import sys
from collections import deque

T = int(input())

for i in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    deq = deque(arr)

    cnt = 0
    flag = True
    if n == 0:
        deq = []

    for j in p:
        if j == 'R':
            cnt += 1
        elif j == 'D':
            if len(deq) < 1:
                flag = False
                print("error")
                break
            else:
                if cnt % 2 == 0:
                    deq.popleft()
                else:
                    deq.pop()
    if flag:
        if cnt % 2 == 0:
            print("[" + ",".join(deq) + "]")
        else:
            deq.reverse()
            print("[" + ",".join(deq) + "]")