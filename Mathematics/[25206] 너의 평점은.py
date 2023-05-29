dic = {"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
answer = 0
total = 0
for _ in range(20):
    tmp = input().split()
    if tmp[2] != "P":
        answer+=float(dic[tmp[2]])*float(tmp[1])
        total+=float(tmp[1])

print(f"{answer/total:.6f}")