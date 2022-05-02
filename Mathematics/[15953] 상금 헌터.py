import sys

a = [10]*21
b = [32]*31

for i in range(15):
    if i == 0:
        a[i] = 500
    elif i in range(1,3):
        a[i] = 300
    elif i in range(3,6):
        a[i] = 200
    elif i in range(6,10):
        a[i] = 50
    elif i in range(10,15):
        a[i] = 30

for i in range(15):
    if i == 0:
        b[i] = 512
    elif i in range(1,3):
        b[i] = 256
    elif i in range(3,7):
        b[i] = 128
    elif i in range(7,15):
        b[i] = 64

num = int(sys.stdin.readline())

for i in range(num):
    answer = 0
    c, d = map(int, sys.stdin.readline().split())
    if c == 0:
        pass
    elif c-1 < 21:
        answer+= a[c-1]
    if d == 0:
        pass
    elif d-1 < 31:
        answer+= b[d-1]
    print(answer*10000)