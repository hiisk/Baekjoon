import sys

for i in range(int(sys.stdin.readline())):
    cnt = 1
    arr = []
    
    N = int(sys.stdin.readline())
    for i in range(N):
        a, b = map(int,sys.stdin.readline().split())
        arr.append([a, b])

    arr.sort()
    tmp = arr[0][1]
    
    for i in range(1,N):
        if tmp > arr[i][1]:
            cnt += 1
            tmp = arr[i][1]

    print(cnt)