num = int(input())

final = []
tmp = 0

import math

for i in range(num):
    H, W, N = map(int, input().split())

    
    tmp = ((N%H))*100 + math.ceil(N//H)+1
    if N%H == 0:
        tmp += H*100 - 1

    final.append(tmp)

for i in range(len(final)):
    print(final[i])