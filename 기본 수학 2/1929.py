# num, target = map(int,input().split())

# arr = []
# tmp = 1
# if num %2 == 0:
#     num-=1
# print(2)

# for i in range(num, target+1, 2):
#     bool = True
    
#     if i == 3 or i == 5 or i ==7 or i == 11:
#         print(i)
#         arr.append(i)
#         continue
#     elif i%3 == 0 or i%5 == 0 or i%7 == 0 or i%11 == 0:
#         continue
#     elif i == 1 :
#         continue
    
#     for j in arr:
#         if i % j == 0:
#             bool = False
#             break
#     if bool:
#         print(i)
#         arr.append(i)

x, y = map(int, input().split())

for i in range(x, y+1):
    if i == 1:
        continue
    for j in range(2, int(i** 0.5)+1 ):
        if i%j==0:
            break
    else:
        print(i)