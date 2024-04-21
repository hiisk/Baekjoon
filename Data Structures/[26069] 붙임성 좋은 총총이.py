answer = []
for i in range(int(input())):
    arr = list(input().split())
    if "ChongChong" in arr:
        answer.extend(arr)
        continue
    for j in arr:
        if j in answer:
            answer.extend(arr)
print(len(set(answer)))