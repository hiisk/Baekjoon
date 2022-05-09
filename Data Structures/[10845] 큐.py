import sys
arr = []

for i in range(int(sys.stdin.readline())):
    tmp = list(sys.stdin.readline().split())
    
    if tmp[0] == "push":
        arr.append(tmp[1])
    elif tmp[0] == "pop":
        if len(arr) > 0:
            print(arr.pop(0))
        else:
            print(-1)
    elif tmp[0] == "size":
        print(len(arr))
    elif tmp[0] == "empty":
        if len(arr) > 0:
            print(0)
        else:
            print(1)
    elif tmp[0] == "front":
        if len(arr) > 0:
            print(arr[0])
        else:
            print(-1)
    elif tmp[0] == "back":
        if len(arr) > 0:
            print(arr[-1])
        else:
            print(-1)