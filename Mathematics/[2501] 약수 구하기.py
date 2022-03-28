n, k = map(int, input().split())
tmp = 0

for i in range(1, n+1):
    if n % i == 0:
        tmp+=1
    if k == tmp:
        print(i)
        break
    
    if n == i:
        print(0)
