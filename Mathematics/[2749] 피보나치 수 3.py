num = int(input())

a, b = 0, 1
num = num %(15*100000)
for i in range(num):
    a, b = b % 1000000, (a+b) % 1000000
print(a)