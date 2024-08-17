A, B = map(int,input().split())

arr_a = set(map(int,input().split()))
arr_b = set(map(int,input().split()))

print(len(arr_a-arr_b))
print(*sorted(arr_a-arr_b))

# import sys
# input = sys.stdin.readline
# A, B = map(int,input().split())
# arr_a = sorted(list(map(int,input().split())))
# arr_b = sorted(list(map(int,input().split())))
# answer = []
# i, j = 0, 0

# while A > i and B > j :
#     if arr_a[i] > arr_b[j]:
#         j+=1
#         if B == j-1:
#             answer += arr_a[i:]
#     elif arr_a[i] < arr_b[j]:
#         answer.append(arr_a[i])
#         i+=1
#     else:
#         i+=1
#         j+=1

# if answer:
#     print(len(answer))
#     print(*answer)
# else:
#     print(0)