from itertools import combinations
L, C = map(int, input().split())
tmp = sorted(input().split())
tmp.sort()
answer = combinations(tmp, L)


for i in answer:
    mo = 0
    ja = 0
    for c in i:
        if c in "aeiou":
            mo +=1
        else:
            ja +=1
    
    if mo >=1 and ja >=2:
        print(''.join(i))
