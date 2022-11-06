arr = [list(map(int, input().split())) for _ in range(10)]
cnt = 0

for i in range(5):
    for j in range(5):
        tmp = arr[i+5][j]
        line = 0
        cnt+=1
        for x in range(5):
            for y in range(5):
                if arr[x][y] == tmp:
                    arr[x][y] = 0
                    # 대각선 빙고일 경우
                    if arr[0][0] == arr[1][1] == arr[2][2] == arr[3][3] == arr[4][4]:
                        line+=1
                    if arr[0][4] == arr[1][3] == arr[2][2] == arr[3][1] == arr[4][0]:
                        line+=1

                    tmp_sum = [0,0,0,0,0]
                    for a in range(5):
                        #가로 빙고일 경우
                        if sum(arr[a]) == 0:
                            line+=1
                            if line == 3:
                                print(cnt)
                                exit()
                        
                        for b in range(5):
                            #세로 빙고를 위한 세팅
                            tmp_sum[b]+=arr[a][b]
                    line+=tmp_sum.count(0)
                    if line >=3:
                        print(cnt)
                        exit()