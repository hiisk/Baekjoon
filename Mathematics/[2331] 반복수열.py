a, p = map(int, input().split())

arr = [a]
while 1:
    tmp = 0
    for i in str(a):
        tmp+=int(i)**p
    if tmp not in arr:
        arr.append(tmp)
        a = tmp
    else:
        print(arr.index(tmp))
        break