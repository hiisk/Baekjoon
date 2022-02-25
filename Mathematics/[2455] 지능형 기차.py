tmp = 0
result = 0

for i in range(4):
    a,b = map(int, input().split())
    tmp -= a
    tmp += b
    result = max(tmp,result)

print(result)