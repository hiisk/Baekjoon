import sys
import math
N, K = map(int, sys.stdin.readline().split())
arr = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
answer = 0

for i in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    arr[Y-1][S] +=1
for i in range(len(arr)):
    if arr[i][0] > 0:
        answer += math.ceil(arr[i][0]/K)
    if arr[i][1] > 0:
        answer += math.ceil(arr[i][1]/K)
print(answer)
