while 1:
    tmp = input()
    if tmp == "end": # end일 경우 While문 해제
        break
    tmp = list(tmp)
    
    mo_cnt = 1 # 1번 조건
    three_row = 0 # 2번 조건
    diff = 0 # 3번 조건
    
    for i in range(len(tmp)):
        if tmp[i] in ["a","e","i","o","u"]:
            mo_cnt = 0
        if i > 1:
            if (tmp[i] in ["a","e","i","o","u"] and tmp[i-1] in ["a","e","i","o","u"] and tmp[i-2] in ["a","e","i","o","u"]) or (tmp[i] not in ["a","e","i","o","u"] and tmp[i-1] not in ["a","e","i","o","u"] and tmp[i-2] not in ["a","e","i","o","u"]):
                three_row = 1
        if i > 0:
            if tmp[i] == tmp[i-1] and tmp[i] not in ["e","o"]:
                diff = 1
    if mo_cnt or three_row or diff:
        print("<"+ "".join(tmp)+"> is not acceptable.")
    else:
        print("<"+ "".join(tmp)+"> is acceptable.")