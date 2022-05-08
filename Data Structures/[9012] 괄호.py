import sys
num = int(sys.stdin.readline())

for i in range(num):
    tmp = list(sys.stdin.readline())
    while 1:
        exist = 0
        for j in range(1, len(tmp)):
            if tmp[j-1] == "(" and tmp[j] == ")":
                exist = j
                break
        if exist != 0:
            tmp.pop(j)
            tmp.pop(j-1)
        elif len(tmp) == 1:
            print("YES")
            break
        else:
            print("NO")
            break