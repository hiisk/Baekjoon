import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jew = []
bags = []

for _ in range(N):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()

answer = 0
tmp = []
for i in bags:
    while jew and i >= jew[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jew)[1])
    if tmp:
        answer -= heapq.heappop(tmp)
    elif not jew:
        break
print(answer)