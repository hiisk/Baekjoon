tmp = list(input())
for i in range(1, len(tmp)):
    if tmp[i-1:i+1] == ["X","X"]:
        tmp[i-1:i+1] = ["B","B"]
for i in range(3, len(tmp)):
    if tmp[i-3:i+1] == ["B","B","B","B"]:
        tmp[i-3:i+1] = ["A","A","A","A"]
answer = ""
for i in range(len(tmp)):
    if tmp[i] == "X":
        answer = -1
        break
    else:
        answer += tmp[i]
print(answer)
