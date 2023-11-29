from itertools import combinations

N = int(input())
index, tmp = 0, 0

for i in range(N):
    com = list(combinations(map(int,input().split()), 3))
    for j in com:
        if sum(j)%10 >= tmp:
            tmp = sum(j)%10
            index =i+1

print(index)
