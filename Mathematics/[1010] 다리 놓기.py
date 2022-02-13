T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    answer = 1
    tmp = M-N

    while M > tmp:
        answer *= M
        M -= 1
    while N > 1:
        answer = answer // N
        N -= 1

    print(answer)
