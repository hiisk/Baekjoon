from sys import stdin
input = stdin.readline

T = int(input())
answer = ""
result = [False, False, True] + [True, False] * 5000
for number in range(3, 101, 2):
    if result[number]:
        result[number*2::number] = [False] * len(result[number*2::number])

for tc in range(T):
    N = int(input())
    if N == 4:
        answer += "2 2\n"
        continue
    harf_N = N//2
    if not harf_N % 2:
        harf_N += 1
    for i in range(harf_N, N, 2):
        if result[i] and result[N-i]:
            answer += "{} {}".format(N - i, i) + "\n"
            break
print(answer, end="")



start = int(input())
arr = []

# for i in range(start):
#     num = int(input())
#     arr = []
#     tmp_1 = []
#     tmp_2 = []
#     for x in range(2, num+1):
#         if x == 1:
#             continue
#         for j in range(2, int(num** 0.5)+1):
#             if x%j==0:
#                 break
#         else:
#             arr.append(x)

#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             if arr[i] + arr[j] == num:
#                 tmp_1.append(arr[i])
#                 tmp_2.append(arr[j])
#                 break
#     print(max(tmp_1), min(tmp_2))
        
        
#     if i == 1 or i == 0:
#         continue
#     for j in range(2, int(i** 0.5)+1 ):
#         if i%j==0:
#             break
#     else:
#         arr.append(i)
# for i in range(len(arr)-1):
#     # for j in range()
#     if arr[i] + arr[i+1] == num:
#         print(arr[i], arr[i+1])
#     elif arr[i] * 2 == num:
#         print(arr[i], arr[i])

