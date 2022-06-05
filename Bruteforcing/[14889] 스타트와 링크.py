from cmath import inf
from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
possible = []

for team in list(combinations(members, N//2)):
    possible.append(team)

gap = inf
for i in range(len(possible)//2):
    team = possible[i]
    start = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            start += S[member][k]
            
    team = possible[-i-1]
    link = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            link += S[member][k]
            
    gap = min(gap, abs(start - link))
    
print(gap)