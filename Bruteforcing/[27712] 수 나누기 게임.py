N = int(input())
arr = list(map(int,input().split()))
set_arr = set(arr)
max_arr = max(arr)
answer = [0 for _ in range(max_arr+1)]
for i in arr:
    if i == max_arr: continue
    for j in range(2*i, max_arr+1, i):
        if j in set_arr:
            answer[i] += 1
            answer[j] -= 1
            
for i in arr:
    print(answer[i], end = ' ')