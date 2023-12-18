import sys
input = sys.stdin.readline
arr=[]
for i in range(int(input())):
    tmp = list(map(int,input().split()))
    if tmp[0] == 1:
        arr.append(tmp[1])
    elif tmp[0] == 2:
        if len(arr) > 0:
            print(arr.pop())
        else:
            print(-1)
    elif tmp[0] == 3:
        print(len(arr))
    elif tmp[0] == 4:
        if len(arr) > 0:
            print(0)
        else:
            print(1)
    elif tmp[0] == 5:
        if len(arr) > 0:
            print(arr[-1])
        else:
            print(-1)