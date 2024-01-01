n, score, p = map(int,input().split())
if n == 0:
    print(1)
else:
    arr = list(map(int,input().split()))
    arr.append(score)
    arr.sort(reverse=True)
    if p >= (arr.index(score) + 1):
        if n == p and score <= arr[-1]:
            print(-1)
        else:
            print(arr.index(score)+1)
    else:
        print(-1)