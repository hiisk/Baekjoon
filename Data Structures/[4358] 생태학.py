import sys
dic = {}
cnt = 0
while 1:
    tmp = sys.stdin.readline().rstrip()
    if not tmp:
        break
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1
    cnt+=1
    
answer = sorted(dic)
for i in answer:
    print('%s %.4f'%(i, dic[i]/cnt*100))