from itertools import combinations_with_replacement

N, M = map(int, input().split())
C = combinations_with_replacement(range(1,N+1),M)

for i in C:
    print(' '.join(map(str, i)))