import sys

num = 1
tmp = 0
while True:
    L, P, V = map(int,sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
        break
    
    if V%P >= L:
        tmp =L
    else:
        tmp = V%P
        
    print(f'Case {num}: {(V//P)*L + tmp}')
    num +=1