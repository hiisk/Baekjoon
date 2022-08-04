from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

com = combinations(arr,M)

for i in com:
    print(' '.join(map(str, i)))