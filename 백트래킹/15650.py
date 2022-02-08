from itertools import combinations

N, M = map(int, input().split())
P = combinations(range(1, N+1), M)

for i in P:
    print(' '.join(map(str, i)))