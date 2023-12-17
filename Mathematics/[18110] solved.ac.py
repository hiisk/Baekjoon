import sys
input = sys.stdin.readline
n = int(input())
if n == 0:
    print(n)
    sys.exit()
avg = (int(n*0.15)+1 if (n*0.15)%1>=0.5 else int(n*0.15))
arr = [int(input()) for _ in range(n)]
arr = sorted(arr)[avg:n-avg]
answer = sum(arr)/len(arr)
print(int(answer)+1 if answer%1>=0.5 else int(answer))