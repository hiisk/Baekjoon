A, B = input().split()

tmp_1 = ''
tmp_2 = ''
tmp_3 = ''
tmp_4 = ''

for i in A:
    if i == '6':
        tmp_1 += str(5)
    else:
        tmp_1 += str(i)

for i in A:
    if i == '5':
        tmp_2 += str(6)
    else:
        tmp_2 += str(i)

for i in B:
    if i == '6':
        tmp_3 += str(5)
    else:
        tmp_3 += str(i)

for i in B:
    if i == '5':
        tmp_4 += str(6)
    else:
        tmp_4 += str(i)
print(int(tmp_1)+int(tmp_3), int(tmp_2)+int(tmp_4))