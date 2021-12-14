tmp = int(input())
cnt = 0
count = 0

t = []
for i in range(tmp):
    t = list(map(str , input()))
    for j in range(len(t)):
        if t[j] == 'O':
            cnt +=1
        elif t[j] == 'X':
            cnt = 0
        count +=cnt
    print(count)
    count = 0
    cnt = 0