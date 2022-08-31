N, K = map(int, input().split())
p = 1000000007

def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % p
    return n

def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    
    tmp = square(n, k//2)
    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p

a = factorial(N)
b = factorial(N-K) * factorial(K) % p

print(a * square(b, p-2) % p)
