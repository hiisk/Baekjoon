from math import floor

n, m = map(int,input().split())
z = floor(100 * m/n)
start, end = 0 , 1000000000

if z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2
        tmp_n, tmp_m = n + mid, m + mid
        if floor(100 * tmp_m/tmp_n) > z:
            end = mid - 1
        else:
            start = mid + 1
    print(end + 1)