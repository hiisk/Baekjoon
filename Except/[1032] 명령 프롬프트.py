num = int(input())
answer = list(input())

for _ in range(num-1):
    next = list(input())
    for i in range(len(answer)):
        if answer[i] != next[i] and answer[i] != "?":
            answer[i] = "?"
print(*answer, sep ="")