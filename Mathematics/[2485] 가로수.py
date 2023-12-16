import math
import sys
input = sys.stdin.readline

N = int(input())
answer = 0
pre_tmp = int(input())
tmp = int(input())
arr = [tmp-pre_tmp]
gcd = arr[-1]
for _ in range(2,N):
    next_tmp = int(input())
    pre_tmp = tmp
    dist = next_tmp - tmp
    tmp = next_tmp
    gcd = math.gcd(gcd,dist)
    arr.append(dist)

for i in range(N-1):
    answer += arr[i]//gcd-1

print(answer)