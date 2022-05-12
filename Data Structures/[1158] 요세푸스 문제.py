import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(range(1,8,1))

answer = [] 
num = 0 

for _ in range(N):
    num += K-1  
    if num >= len(arr):
        num = num%len(arr)

    answer.append(str(arr.pop(num)))
print("<",", ".join(answer)[:],">", sep='')