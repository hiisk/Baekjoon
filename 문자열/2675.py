cnt = int(input())
tmp = []
answer = ""

for i in range(cnt):
    tmp = input().split(" ")
    for j in range(len(tmp[1])):
        answer += str(tmp[1][j])*int(tmp[0])
    answer+="\n"

print(answer)