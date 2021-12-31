cnt = int(input())
val = 0

for i in range(cnt):
    tmp = list(input())
    del_tmp = []
    if len(tmp) != 1:
        for j in range(1, len(tmp)):
            if tmp[j-1] == tmp[j]:
                del_tmp.append(tmp[j])
        if len(tmp) - len(del_tmp) == len(set(tmp)):
            val += 1
    else:
        val += 1
print(val)