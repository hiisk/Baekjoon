num = int(input())

# a = 0
# b = 1
# answer = 0

# for _ in range(num-1):
#     a%= 1000000
#     b%= 1000000
#     answer = a + b
#     tmp = b
#     b = b+a
#     a = tmp

fibo = lambda n: 1 if n <= 2 else fibo(n-1) + fibo(n-2)

print(fibo(num)) 