import sys
import heapq

n, p = map(int, sys.stdin.readline().split())
stack = [[] for _ in range(7)]
answer = 0

for _ in range(n):
    j, f = map(int, sys.stdin.readline().split())

    if not stack[j]:
        heapq.heappush(stack[j], f)
        answer += 1

    elif stack[j][-1] < f:
        heapq.heappush(stack[j], f)
        answer += 1

    elif stack[j][-1] > f:
        while 1:
            if not stack[j]:
                answer += 1
                stack[j].append(f)
                break
            if stack[j][-1] <= f:
                if stack[j][-1] < f:
                    heapq.heappush(stack[j], f)
                    answer += 1
                break

            stack[j].pop()
            answer += 1

print(answer)