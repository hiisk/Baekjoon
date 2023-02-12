import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

ans = [0,0]
for i in range(n):
    x,y = 0,0
    for j in range(n):
        if arr[i][j] == '.':
            x+=1
        else:
            x=0
        if x==2:
            ans[0] += 1
        
        if arr[j][i] == '.':
            y+=1
        else:
            y=0
        if y==2:
            ans[1] += 1
print(*ans)