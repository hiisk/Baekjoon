n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

value = price[0]
answer = 0

for i in range(n-1):
    if value > price[i]:
        value = price[i]
    answer += (value * dis[i])
    
print(answer)