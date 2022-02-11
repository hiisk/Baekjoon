N, d = map(int, input().split())
N +=1
cnt = 0
answer = 0

while True:
    n = N
    cnt = 0
    tmp = []
    while True:
        cnt +=1
        if n < d**cnt:
            cnt-=1
            break

    for i in range(cnt+1):
        if (n//(d**(cnt-i)))!=n:
            tmp.append(n//(d**(cnt-i)))
            n = n - (d**(cnt-i))*(n//(d**(cnt-i)))
        elif n < d:
            tmp.append(n)

        if len(set(tmp)) != len(tmp) or len(tmp) > d or N > 10**9:
            break

    if N > 10**9 or d < len(tmp):
        print(-1)
        break
    elif len(set(tmp)) == len(tmp):
        for i in range(len(tmp)):
            answer += tmp[i]*d**(cnt-i)
        print(answer)
        print(tmp)
        break
    else:
        tmp[-1] += 1
        N = 0
        for i in range(len(tmp)):
            N += tmp[i]*d**(cnt-i)