import sys

num = int(sys.stdin.readline())
arr = []

for _ in range(num):
    tmp = int(sys.stdin.readline())
    if tmp > 0:
        arr.append(tmp)
    else:
        arr.pop(-1)
print(sum(arr))