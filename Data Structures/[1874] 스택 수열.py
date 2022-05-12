import sys

n = int(sys.stdin.readline())
stack = []
answer = []
flag = True
tmp = 1

for i in range(n):
    num = int(sys.stdin.readline())
    while tmp <= num:
        stack.append(tmp)
        answer.append("+")
        tmp += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:                  
        print("NO")
        flag = False
        break               

if flag:
    print(*answer, sep="\n")