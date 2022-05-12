import sys

n = int(sys.stdin.readline())
stack = []
answer = []
flag = True
cur = 1

for i in range(n):
    num = int(sys.stdin.readline())
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:                  
        print("NO")
        flag = False
        break               

if flag:
    for i in answer:
        print(i)