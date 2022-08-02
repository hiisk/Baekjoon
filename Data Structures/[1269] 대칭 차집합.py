a, b = map(int, input().split())

arr = []

for _ in range(2):
    arr = arr + list(map(int, input().split()))
tmp = len(arr)

print(tmp - (tmp - len(set(arr)))*2)