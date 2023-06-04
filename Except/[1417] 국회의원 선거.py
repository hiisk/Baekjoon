arr = []
num = int(input())
dasom = int(input())
cnt = 0

for _ in range(num-1):
    arr.append(int(input()))
arr.sort(reverse=True)

if num == 1:
  print(0)
else:
  while arr[0] >= dasom:
    dasom += 1
    arr[0] -= 1
    cnt += 1
    arr.sort(reverse=True)
  print(cnt) 