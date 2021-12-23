tmp = list(input().upper())
count_tmp = [0]*26
cnt = 0
for i in range(len(tmp)):
    count_tmp[ord(tmp[i])-65] +=1

for i in range(len(count_tmp)):
    if count_tmp[i] == max(count_tmp):
        cnt +=1
print(cnt)
if cnt > 1:
    print("?")
else:
    print(chr(count_tmp.index(max(count_tmp))+65))