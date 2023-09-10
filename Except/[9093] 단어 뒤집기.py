num = int(input())

for _ in range(num):
    tmp = input().split()
    answer = ""
    for i in tmp:
        answer += i[::-1]+" "
    print(answer)