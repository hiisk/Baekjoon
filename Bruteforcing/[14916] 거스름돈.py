def coin(num):
    if num in [1,3]:
        print(-1)
        return
    tmp = num%5
    if tmp % 2 == 1:
        print(int(num//5)-1+int(tmp+5)//2)
    else:
        print(int(num//5)+ int(tmp//2))

num = int(input())
coin(num)