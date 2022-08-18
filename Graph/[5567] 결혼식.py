import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[] for _ in range(n+1)]
answer = set()

for i in range(m):
    x, y = map(int,sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

if not arr[1]:
    print(0)
else:
    for i in arr[1]:
        answer.add(i)
        if arr[i]:
            for j in arr[i]:
                answer.add(j)
    print(len(answer)-1)