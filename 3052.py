tmp = []
for i in range(10):
    tmp.append(int(input())%42)
print(len(set(tmp)))