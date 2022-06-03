from itertools import permutations
num = int(input())

arr = list(input().split())
answer = list(map(' '.join, permutations(arr)))
value = 0

for i in range(len(answer)):
    tmp = list(map(int, answer[i].split()))
    tmpval = 0
    for j in range(1, len(tmp)):
        tmpval += abs(tmp[j-1] - tmp[j])
    value = max(value, tmpval)
print(value)