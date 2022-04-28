import sys

N = int(input())
answer = 0

for i in range(N):
    tmp = 0
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b and b == c and a == c:
        tmp = (10000 + 1000*a)
    elif a == b:
        tmp = (1000 + 100*a)
    elif b == c:
        tmp = (1000 + 100*b)
    elif c == a:
        tmp = (1000 + 100*c)
    else:
        tmp = (max(a,b,c)*100)
    
    if answer < tmp:
        answer = tmp
print(answer)