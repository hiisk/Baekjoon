import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
arr = sorted(list(map(int, input().split())))

i = 0
j = N-1
cnt = 0
while 1:
    if i >= j:
        print(cnt)
        break
    tmp = arr[i] + arr[j]
    if tmp > M:
        j-=1
    elif tmp == M:
        cnt+=1
        i+=1
        j-=1
    else:
        i+=1