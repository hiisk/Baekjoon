import sys
input = sys.stdin.readline
num = int(input())
arr = []

for _ in range(num):
    arr.append(int(input()))
tmp = arr[-1]
cnt = 1

for i in range(num-2, -1, -1):
    if tmp < arr[i]:
        cnt+=1
        tmp = arr[i]
print(cnt)