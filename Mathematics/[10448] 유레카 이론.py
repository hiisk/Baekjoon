import sys
cnt = 1
arr = []
while 1:
    if cnt*(cnt+1)//2 > 1000:
        break
    arr.append(cnt*(cnt+1)//2)
    cnt+=1

num = int(sys.stdin.readline())

for i in range(num):
    K = int(sys.stdin.readline())
    bool = False
    for j in range(len(arr)):   
        if arr[j] >= K:
            tmp = j
            break
        else:
            tmp = j
    for x in range(len(arr[:tmp])):
        for y in range(x, len(arr[:tmp])):
            for z in range(y, len(arr[:tmp])):
                if K == arr[x]+arr[y]+arr[z]:
                    bool = True
                    break
            if bool:
                break
        if bool:
            break
    if bool:
        print(1)
    else:
        print(0)