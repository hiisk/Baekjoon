S = input()
answer = ''

for i in range(len(S)):
    if(S[i].isalpha()): #알파벳인지 확인
        tmp = ord(S[i])+13
        if (ord(S[i])> 96 and tmp > 122) or (ord(S[i]) < 91 and tmp > 90): #대문자, 소문자를 구별해서 값을 구한다.
            tmp-=26
        answer += chr(tmp)
    else:
        answer += S[i]
print(answer)