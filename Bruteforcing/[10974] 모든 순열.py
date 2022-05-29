from itertools import permutations
arr = [str(i) for i in range(1, int(input())+1)]
answer = list(map(' '.join, permutations(arr)))
print(*answer, sep="\n")