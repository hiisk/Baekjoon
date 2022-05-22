from collections import Counter
from math import ceil

num = input()

tmp = Counter(list(num))
arr = []

for i in range(10):
    if tmp[str(i)]:
        arr.append(tmp[str(i)])
    else:
        arr.append(0)

print(max(max(arr[:6]),max(arr[7:9]),ceil((arr[6]+arr[9])/2)))