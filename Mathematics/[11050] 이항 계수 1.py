N, K = map(int, input().split())
answer = 1

for i in range(1, K+1):
    answer *=((N-i+1)/i)
print(int(answer))