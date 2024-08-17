from itertools import permutations
import sys
inpurt = sys.stdin.readline
n = int(input())
k = int(input())
arr = []
answer = []

for i in range(n):
    arr.append(int(input()))
tmp = list(permutations(arr,k))

for i in range(len(tmp)):
    tmp_str = ""
    for j in range(len(tmp[i])):
        tmp_str += str(tmp[i][j])
    answer.append(tmp_str)
print(len(set(answer)))