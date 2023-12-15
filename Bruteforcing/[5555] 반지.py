st = input()
n = int(input())
answer = 0
for _ in range(n):
    tmp = input()
    tmp = tmp + tmp[:len(st)-1]
    if st in tmp:
        answer+=1
print(answer)