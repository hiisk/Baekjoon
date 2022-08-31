import sys
import heapq

n = int(sys.stdin.readline())

left = []
right= []
answer = []

for i in range(n):

    num = int(sys.stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    if right and left[0][1] > right[0][0]:
        a = heapq.heappop(right)[0]
        b = heapq.heappop(left)[1]
        heapq.heappush(left, (-a, a))
        heapq.heappush(right, (b, b))

    answer.append(left[0][1])

print(*answer, sep="\n")
