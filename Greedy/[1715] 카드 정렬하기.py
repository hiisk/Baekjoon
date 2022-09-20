import heapq
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(sys.stdin.readline()))

if len(arr) == 1:
    print(0)
else:
    answer = 0
    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        answer += a + b
        heapq.heappush(arr, a + b)
    print(answer)