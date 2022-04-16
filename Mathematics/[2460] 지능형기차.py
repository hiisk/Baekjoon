num = 0
answer = 0

for _ in range(10):
    tmp_1, tmp_2 = map(int, input().split())
    num += (tmp_2 - tmp_1)
    answer = max(answer, num)
    
print(answer)