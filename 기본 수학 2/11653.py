num = int(input())

i = 1
while True:
    i += 1
    if num == 1:
        break
    elif num/i == num//i:
        print(i)
        num/=i
        i = 1