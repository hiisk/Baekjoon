T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    result = []
    for i in range(1, int(a**0.5)+2):
        if a%i==0:
            result.append(i)
    if a > 2:
        result.append(a)
    
    print(result)

# real answer
for _ in range(int(input())):
    a, b = map(int, input().split())

print("yes")