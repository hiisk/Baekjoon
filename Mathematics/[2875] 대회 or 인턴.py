n, m, k = map(int, input().split())

answer = 0

for i in range(k+1):
    if answer < (n-i)//2 and answer < m-k+i:
        answer = min((n-i)//2, m-k+i)
print(answer)