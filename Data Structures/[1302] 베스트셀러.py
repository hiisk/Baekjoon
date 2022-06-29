import sys
n = int(sys.stdin.readline().rstrip())
dic = {}

for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    if tmp in dic:
        dic[tmp] +=1
    else:
        dic[tmp] = 1

answer = sorted(dic.items(),key = lambda x : (-x[1],x[0]))
print(answer[0][0])