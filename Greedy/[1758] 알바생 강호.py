import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*N

for i in range(N):
    arr[i] = int(input())

arr.sort(reverse=True)
tmp = 0
answer = 0

for i in range(N):
    if (arr[i]-tmp) > 0:
        answer += arr[i] - tmp
        tmp +=1
    else:
        break

print(answer)