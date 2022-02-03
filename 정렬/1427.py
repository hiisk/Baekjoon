tmp = str(input())
num = []

for i in range(len(tmp)):
    num.append(int(tmp[i]))

num.sort(reverse = True)

for i in num:
    print(i, end="")