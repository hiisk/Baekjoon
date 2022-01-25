num = int(input())

target = 0

for i in range(1, num+1):
    if i + sum(map(int, list(str(i)))) == num:
        target = i
        break
print(target)