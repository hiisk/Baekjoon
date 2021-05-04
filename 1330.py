values = input()
values = values.split()
a = int(values[0])
b = int(values[1])
# 코드 작성: A와 B를 비교하여 결과 출력
if(a > b):  print(">")
elif(a == b):   print("==")
else:   print("<")