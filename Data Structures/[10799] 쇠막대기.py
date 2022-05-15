# 시간초과
import sys

tmp = sys.stdin.readline()

laser = []
left = []
right = []
answer = 0

for i in range(1, len(tmp)):
    if tmp[i-1] == "(" and tmp[i] == ")":
        laser.append(i)
    elif tmp[i-1] == "(":
        left.append(i)
    elif tmp[i] == ")":
        right.append(i)

for a, b in zip(left,right):
    tmp = 1

    for i in laser:
        if a < i < b:
            tmp+=1
    answer+=tmp
print(answer)

# 정답
laser = list(input())
answer = 0
arr = []

for i in range(len(laser)):
    if laser[i] == '(':
        arr.append('(')

    else:
        if laser[i-1] == '(': 
            arr.pop()
            answer += len(arr)

        else:
            arr.pop() 
            answer += 1 
print(answer)