import sys
num = int(input())

for _ in range(num):
    cnt = 0
    M,N,x,y = map(int, sys.stdin.readline().split())
    while True:
        cnt+=1
        if cnt%M == x and cnt%N == y:
            print(cnt)
            break
        elif M*N < cnt:
            print(-1)
            break


import sys
input = sys.stdin.readline

num = int(input())

for _ in range(num):
    m,n,x,y = map(int,input().split())
    ans = -1
    while x <= m*n:
        if (x-y) % n == 0:
            ans = x
            break
        x += m
    print(ans)