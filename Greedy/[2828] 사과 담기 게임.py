N, M = map(int, input().split())
J = int(input())

current = 1
cnt = 0

for i in range(J):
    apple = int(input())
    if current <= apple <= current+M-1:
        continue
    elif apple < current:
        cnt += current-apple
        current -= current-apple
    else:
        cnt += apple - (current+M-1)
        current += apple - (current+M-1)
print(cnt)