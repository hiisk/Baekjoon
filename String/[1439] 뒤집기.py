s = input()
cnt = 0 
target = ""

for i in s:
    if i != target:
        target = i
        cnt += 1

print((cnt)//2)