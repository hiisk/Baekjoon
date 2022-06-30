import sys

n, m, b = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
answer = sys.maxsize
height = 0

for target in range(257):
    max_target, min_target = 0, 0

    for i in range(n):
        for j in range(m):

            if graph[i][j] >= target:
                max_target += graph[i][j] - target
            else:
                min_target += target - graph[i][j]

    if max_target + b >= min_target:
        if min_target + (max_target * 2) <= answer:
            answer = min_target + (max_target * 2)
            height = target
    else:
        break

print(answer, height)