import sys
input = sys.stdin.readline
n, k = map(int,input().split())
arr = list(map(int, input().split()))
answer =[]
answer.append(sum(arr[:k]))
for i in range(n - k):
    answer.append(answer[i] - arr[i] + arr[k+i])
print(max(answer))