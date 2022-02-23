A, B = map(int,input().split())
C = int(input())
tmp = 0

B += C%60
tmp = B//60
B = B%60

A += C//60
A = (A+tmp)%24

print(A, B)