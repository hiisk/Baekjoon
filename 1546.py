arr = int(input())
tmp = input().split()
max_arr = int(max(tmp))

for i in range(arr):
    tmp[i] = int(tmp[i])/max_arr*100

print(sum(tmp)/arr)