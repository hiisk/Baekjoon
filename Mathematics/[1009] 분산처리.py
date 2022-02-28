T = int(input())


for _ in range(T):
    a, b = map(int, input().split())    
    
    tmp = b%4
    if tmp == 0:
        tmp = 4

    answer = a**(tmp)%10

    if answer == 0:
        answer = 10
    print(answer)