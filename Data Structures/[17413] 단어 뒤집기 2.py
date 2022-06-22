S = input()
tmp = ""
answer = ""

type = True

for i in S:
    if i == "<":
        answer+= tmp[::-1]
        tmp = ""
        answer+= "<"
        type = False
    elif i == ">":
        answer+= tmp
        tmp = ""
        answer+= ">"
        type = True
    elif i == " " and type:
        answer+= tmp[::-1] +" "
        tmp = ""
    else:
        tmp+=i

if tmp:
    answer+= tmp[::-1]

print(answer)