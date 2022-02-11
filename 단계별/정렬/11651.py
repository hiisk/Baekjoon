import sys
num = int(input())

arr = []
for i in range(num):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([y,x])

arr.sort()
for i in range(len(arr)):
    print(arr[i][1], arr[i][0])