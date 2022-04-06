import math
n, a, b = map(int,input().split())
num = 1
while True:
    n = math.ceil(n/2)
    if n ==1:
        break
    num+=1

answer = 0
while True:
    if answer > num:
        print(-1)
        break

    if a == b :
        print(answer)
        break
    else:
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer+=1