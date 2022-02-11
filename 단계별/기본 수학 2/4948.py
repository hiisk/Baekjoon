# arr = []

# while True:
#     num = int(input())
#     target = num * 2
#     cnt = 0
#     if num == 0 or num > 123456:
#         break
#     elif num == 1:
#         cnt +=1
#         arr.append(cnt)
#         continue
    
#     for i in range(num, target+1):
#         bool = True
#         for j in range(2, int(i**0.5)+1):
#             if i%j==0:
#                 bool = False
#                 break
#         if bool == False:
#             continue
#         elif bool:
#             cnt+=1

#     if cnt !=0:
#         arr.append(cnt)
#         cnt = 0

# print("\n".join(map(str, arr)))

# from math import sqrt
# while True:
#     n = int(input())
#     if n == 0:
#         break
    
#     cnt = 0

#     for i in range(n+1, 2*n+1):
#         if i == 1:
#             continue
#         elif i == 2:
#             cnt += 1
#             continue
#         else:
#             for j in range(2, int(sqrt(i)+1)):
#                 if i % j == 0:
#                     break
#             else:
#                 cnt += 1

#     print(cnt)

import math

def checkValue(n):
    if n == 1:
        return True
    else:
        for i in range(2, int(math.sqrt(number))+1):
            if n % i == 0:
                return False
    return True
 
value = list(range(123456*2))
prime_number = list()
 
for number in value:
    if checkValue(number):
        prime_number.append(number)

while True:
    num = int(input())
    cnt = 0
 
    if num == 0:
        break
 
    for value in prime_number:
        if num < value <= num*2:
            cnt += 1
    print(cnt)