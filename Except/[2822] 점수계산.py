arr = [int(input()) for _ in range(8)]
tmp = sorted(arr)
answer = []
print(sum(tmp[3:]))
for i in range(5):
    answer.append(arr.index(tmp[3+i])+1)
answer.sort()    
print(*answer)
