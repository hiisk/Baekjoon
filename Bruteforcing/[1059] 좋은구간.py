L = int(input())
num = list(map(int, input().split()))
target = int(input()) # == n

num.append(0)
num.sort()

answer = 0
for i in range(L):
    if num[i] == target or num[i+1] == target:
        answer = 0
        break
    elif num[i] < target and target < num[i+1]:
        answer = (target - num[i]) * (num[i+1] - target) - 1
        break

print(answer)
