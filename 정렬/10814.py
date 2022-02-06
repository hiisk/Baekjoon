import sys
num = int(input())

arr = []

for _ in range(num):
    x, y = sys.stdin.readline().split()
    arr.append([int(x),y])

for i in range(1,201):
    for j in range(len(arr)):
        if i == arr[j][0]:
            print(arr[j][0], arr[j][1])
