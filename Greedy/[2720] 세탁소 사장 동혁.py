coin = [25, 10, 5, 1]
for _ in range(int(input())):
    num = int(input())
    for i in coin:
        print(int(num//i), end=" ")
        num %=i