n = int(input())
switch = list(map(int,input().split()))

for i in range(int(input())):
    x, y = map(int,input().split())
    if x == 1:
        for j in range(y-1,n,y):
            if switch[j] == 0:
                switch[j] = 1
            else:
                switch[j] = 0
    else:
        tmp = 1
        if switch[y-1] == 0:
            switch[y-1] = 1
        else:
            switch[y-1] = 0
        while True:
            if -1 < y-1-tmp and y-1+tmp < n:
                if switch[y-1-tmp] == switch[y-1+tmp]:
                    if switch[y-1-tmp] == 0:
                        switch[y-1-tmp] = 1
                        switch[y-1+tmp] = 1
                    elif switch[y-1-tmp] == 1:
                        switch[y-1-tmp] = 0
                        switch[y-1+tmp] = 0
                    tmp+=1
                else:
                    break
            else:
                break
for i in range(n):
    print(switch[i], end=" ")
    if (i+1)%20==0:
        print()