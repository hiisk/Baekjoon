N, K = map(int, input().split())

mod = 1000000000 
answer = [1] 
answer += [0] * N 
for _ in range(1, K+1): 
    for i in range(1, N+1): 
        answer[i] = (answer[i] + answer[i-1])%mod

print(str(answer[N]))