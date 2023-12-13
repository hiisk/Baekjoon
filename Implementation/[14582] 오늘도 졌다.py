arr_ul = list(map(int,input().split()))
arr_st = list(map(int,input().split()))
check = False
for i in range(9):
    if sum(arr_ul[:i+1]) > sum(arr_st[:i]):
        check = True
        break
print("Yes" if check else "No")