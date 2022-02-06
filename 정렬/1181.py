import sys
num = int(input())

arr = []
cnt = 1

for _ in range(num):
    x = sys.stdin.readline()
    if x not in arr:
        arr.append(x)

arr.sort()
for i in range(1,51):
    for j in range(len(arr)):
        if len(arr[j][:-1]) == i:
            print(arr[j][:-1])