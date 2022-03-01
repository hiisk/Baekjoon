X = int(input())
arr = [64, 32, 16, 8, 4, 2, 1]
answer = 0

for i in arr:
    if X >= i:
        X -= i
        answer +=1

print(answer)