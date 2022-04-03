import sys
num = int(input())
answer = 0

for _ in range(num):
    answer += int(sys.stdin.readline())
print(answer - (num - 1))