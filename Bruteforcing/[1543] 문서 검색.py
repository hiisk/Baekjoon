a = list(input())
b = list(input())
answer = 0
i = 0

while i <= len(a)-len(b):
    if a[i:len(b)+i] == b:
        answer+=1
        i += len(b)
    else:
        i += 1
print(answer)
