import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
K = int(input())

for _ in range(K):
    answer = 0
    i,j,x,y = map(int, input().split())
    for a in range(i-1, x):
        for b in range(j-1, y):
            answer += arr[a][b]
    print(answer)