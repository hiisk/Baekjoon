from itertools import combinations 

while True:
    tmp = list(map(int, input().split()))
    answer = list(combinations(tmp[1:], 6))

    if tmp[0] != 0:
        for i in range(len(answer)):
            for j in range(6):
                if j ==5:
                    print(answer[i][j])
                else:
                    print(answer[i][j], end=" ")
        print("")
    else:
        break