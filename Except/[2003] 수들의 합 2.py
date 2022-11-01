n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
cnt = 0

while end < n and start < n:
    if sum(arr[start:end+1]) < m:
        end += 1
    elif sum(arr[start:end+1]) == m:
        cnt += 1
        if start < end:
            start += 1
        else:
            end += 1
    else:
        start += 1

print(cnt)
