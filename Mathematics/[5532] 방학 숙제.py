L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

tmp_1 = 0
tmp_2 = 0

if A%C == 0:
    tmp_1 = A//C
else:
    tmp_1 = A//C +1

if B%D == 0:
    tmp_2 = B//D
else:
    tmp_2 = B//D +1
print(L - max(tmp_1,tmp_2))