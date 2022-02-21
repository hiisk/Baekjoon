from itertools import combinations
L, C = map(int, input().split())
tmp = sorted(input().split())
tmp.sort()
answer = combinations(tmp, L)


for i in answer:
    num_v = 0
    num_c = 0
    for c in i:
        if c in "aeiou": #모음이 있는지 확인
            num_v +=1
        else:
            num_c +=1
    
    if num_v >=1 and num_c >=2:
        print(''.join(i))
