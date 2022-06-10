import heapq, sys

heap = []

num = int(sys.stdin.readline())
for i in range(num):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(tmp),tmp))