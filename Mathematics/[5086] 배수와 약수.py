import sys

while True:
    a, b = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0:
        break
    elif int(b//a) == b/a:
        print("factor")
    elif int(a//b) == a/b:
        print("multiple")
    else:
        print("neither")