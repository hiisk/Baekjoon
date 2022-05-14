import sys
import re

while 1:
    tmp = sys.stdin.readline()
    if tmp[0] == ".":
        break
    
    tmp = re.sub(r'[a-zA-Z0-9]',"",tmp)
    tmp = list(re.sub(r' ',"",tmp))
    while len(tmp)>2:
        for i in range(1, len(tmp)):
            if (tmp[i-1] == "[" and tmp[i] == "]") or (tmp[i-1] == "(" and tmp[i] == ")"):
                tmp.pop(i)
                tmp.pop(i-1)
                break
            elif i == len(tmp)-1:
                tmp = []
                break
    if len(tmp)==2:
        print("yes")
    else:
        print("no")
