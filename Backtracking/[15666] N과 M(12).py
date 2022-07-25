from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

com = list(set(combinations_with_replacement(arr,M)))
com.sort()

for i in com:
    print(' '.join(map(str, i)))
