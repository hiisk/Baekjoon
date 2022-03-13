import sys

while True:
    tmp = int(sys.stdin.readline())
    if tmp ==0:
        break
    for i in range(3, tmp, 2):
        bool = True

        if i%2 !=0:
            for j in range(3, tmp-i, 2):

                if (tmp-i)%j ==0:
                    bool=False
                    break

        if bool:
            print(f'{tmp} = {i} + {tmp-i}')
            break


from sys import stdin

array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

while True:
    n = int(stdin.readline())

    if n == 0: break

    for i in range(3, len(array)):
        if array[i] and array[n-i]:
            print(n, "=", i, "+", n-i)
            break