import sys
num = int(sys.stdin.readline())

answer = set()

for _ in range(num):
    tmp = list(sys.stdin.readline().split())
    if len(tmp)>1:
        tmp[1] = int(tmp[1])

    if tmp[0] == "add" and tmp[1] not in answer:
        answer.add(tmp[1])
    elif tmp[0] == "remove" and tmp[1] in answer:
        answer.discard(tmp[1])
    elif tmp[0] == "check":
        if tmp[1] in answer:
            print(1)
        else:
            print(0)
    elif tmp[0] == "toggle":
        if tmp[1] in answer:
            answer.discard(tmp[1])
        else:
            answer.add(tmp[1])
    elif tmp[0] == "all":
        answer = {i for i in range(1, 21)}
    elif tmp[0] == "empty":
        answer = set()