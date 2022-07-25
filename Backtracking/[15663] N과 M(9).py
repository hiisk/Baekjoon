from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

per = list(set(permutations(arr,M)))
per.sort()

for i in per:
    print(' '.join(map(str, i)))
