import sys
num = int(sys.stdin.readline())

for _ in range(num):
    r, e, c = map(int, sys.stdin.readline().split())
    tmp = e - c - r
    
    if tmp > 0:
        print("advertise")
    elif tmp == 0:
        print("does not matter")
    else:
        print("do not advertise")