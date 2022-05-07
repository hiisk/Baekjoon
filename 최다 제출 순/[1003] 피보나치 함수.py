import sys
def fib(n):
    if n == 0:
        global count_0
        count_0 +=1
        return 0
    elif n == 1:
        global count_1
        count_1 +=1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

T = int(sys.stdin.readline())
for _ in range(T):
    count_0 = 0
    count_1 = 0
    N = int(sys.stdin.readline())
    fib(N)
    print(count_0, count_1)
# ---------------------------------
t = int(input())
 
for _ in range(t):
    cnt_0 = [1,0]
    cnt_1 = [0,1]
    n = int(input())
    if n>1:
        for i in range(n-1):
            cnt_0.append(cnt_1[-1])
            cnt_1.append(cnt_0[-2]+cnt_1[-1]) 
 
    print(cnt_0[n], cnt_1[n])