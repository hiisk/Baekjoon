arr = [True for _ in range(4000001)]

for i in range(2, int(4000001 ** 0.5)):
    if arr[i]:
        for j in range(i+i, 4000001, i):
            arr[j] = False 
tmp = [i for i, j in enumerate(arr) if j == True and i >=2 ]

tmp_2 = [0] * (len(tmp) + 1)
for i in range(len(tmp)):
    tmp_2[i+1] = tmp_2[i] + tmp[i] 
    
N = int(input())

answer = 0
start = 0
end = 1

while start < len(tmp_2) and tmp[end-1] <= N:
    if tmp_2[end] - tmp_2[start] == N:
        answer += 1
        start += 1
    elif tmp_2[end] - tmp_2[start] > N:
        start += 1
    else:
        if end < len(tmp_2) - 1:
            end += 1
        else:
            start += 1

print(answer)