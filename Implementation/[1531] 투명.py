N, M = map(int,input().split())
arr = [[0]*100 for _ in range(100)]

answer = 0
for _ in range(N):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            arr[i-1][j-1] += 1

for i in range(100):
    for j in range(100):
        if arr[i-1][j-1] > M:
            answer+=1

print(answer)