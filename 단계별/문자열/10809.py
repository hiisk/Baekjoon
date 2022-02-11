tmp = list(input())
arr = [-1]*26
answer =""
for i in range(len(tmp)):
    if arr[ord(tmp[i])-97] == -1:
        arr[ord(tmp[i])-97] = i

for i in range(len(arr)):
    answer += str(arr[i]) +" "

print(answer)