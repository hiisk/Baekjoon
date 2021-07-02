h,m = map(int,input().split())

if h<45:
    if h == 0:
        h = h+23
        m = m+15
        print(h, m)
    else:
        m = m+15
        print(h-1, m)
elif(m >= 45):
    m = m - 45
    print(h, m)