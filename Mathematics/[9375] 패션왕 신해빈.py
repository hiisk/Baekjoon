num = int(input())

for _ in range(num):
    dic = {}
    tmp = int(input())
    for _ in range(tmp):
        cloth, type = input().split()
        if type not in dic:
            dic[type] = 1
        else:
            dic[type] +=1
    answer = 1
    for i in dic.values():
        answer*=(i+1)
    print(answer-1)