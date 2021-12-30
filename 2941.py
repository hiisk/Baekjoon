arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
tmp = input()
cnt = 0

for i in range(len(arr)):
    if arr[i] in tmp:
        tmp = tmp.replace(arr[i],"1")
cnt+=len(tmp)
print(cnt)