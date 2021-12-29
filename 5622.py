tmp = list(input())

sum = 0
for i in range(len(tmp)):
    if ord(tmp[i]) < 80:
        sum += (ord(tmp[i])-2)//3-21+3
    elif ord(tmp[i]) in (80,81,82,83):
        sum += 8
    elif ord(tmp[i]) in (84,85,86):
        sum += 9
    else:
        sum += 10

print(sum)