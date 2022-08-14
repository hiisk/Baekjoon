import sys
num = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(num):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    arr = arr + tmp
    arr.sort(reverse=True)
    arr = arr[:num]
print(arr[num-1])