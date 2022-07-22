n, k = map(int, input().split())

arr = [0]*n
answer = 0

for i in range(n):
    arr[i] = int(input())

arr.sort(reverse = True)

for i in arr:
    answer += int(k//i)
    k = k % i

print(answer)