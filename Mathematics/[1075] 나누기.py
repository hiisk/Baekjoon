N = int(input())
F = int(input())
N -=(N%100)
for i in range(100):
    if N%F == 0:
        if i <= 9:
            print("0"+str(i))
            break
        else:
            print(str(i))
            break
    N+=1