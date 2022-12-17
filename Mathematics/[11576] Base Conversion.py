from collections import deque
a, b = map(int,input().split())
num = int(input())
arr = list(map(int,input().split()))
tmp = 0
deq = deque()

for i in range(1, num+1):
    tmp += arr[-i]*a**(i-1)
deq.append(int(tmp//b))
deq.append(int(tmp%b))

while 1:
    if deq[0] > b-1:
        deq.appendleft(int(deq[0]//b))
        deq[1] = deq[1]%b
    else:
        break
print(*deq)