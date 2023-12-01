import sys
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lan:
        cnt += i // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)