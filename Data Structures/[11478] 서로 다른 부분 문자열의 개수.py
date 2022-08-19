a = input()
answer = set()

for i in range(len(a)):
    for j in range(len(a)-i):
        answer.add(a[j:j+i+1])

print(len(answer))