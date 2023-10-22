a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in range(a):
    if b >= arr[i]:
        b+=1

print(b)
