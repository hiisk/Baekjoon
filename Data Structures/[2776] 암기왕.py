T = int(input())

for i in range(T):
    N = int(input())
    N_array = list(map(int,input().split()))
    M = int(input())
    M_array = list(map(int,input().split()))

    dic = {}
    for i in M_array:
        dic[i] = 0
    for i in N_array:
        if i in dic:
            dic[i] = 1

    for i in M_array:
        if dic[i] == 1:
            print(1)
        else:
            print(0)