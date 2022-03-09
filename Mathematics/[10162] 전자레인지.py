tmp = int(input())

a = 0
b = 0 
c = 0

if tmp%10 != 0:
    print(-1)
else:
    a = tmp//300
    tmp -= a*300
    b = tmp//60
    tmp -= b*60
    c = tmp//10
    print(a, b, c)