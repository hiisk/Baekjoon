num = int(input())
data = list(map(int, input().split()))

for i in range(num-1, 0, -1):
    if data[i-1] < data[i]:
        for j in range(num-1, 0, -1):
            if data[i-1] < data[j]:
                data[i-1], data[j] = data[j], data[i-1]
                data = data[:i] + sorted(data[i:])
                for i in data:
                    print(i, end=' ')
                exit()
print(-1)