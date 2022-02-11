import sys
import statistics
from collections import Counter

num = int(input())
arr = []
for _ in range(num):
    arr.append(int(sys.stdin.readline()))

# 산술평균
sys.stdout.write(str(round(statistics.mean(arr))) + '\n')

# 중앙값
sys.stdout.write(str(statistics.median(arr)) + '\n')

# 최빈값
cnt = Counter(arr).most_common()
mode = []
for i in cnt:
    if i[1] == cnt[0][1]:
        mode.append(i[0])
    else:
        break
if len(mode) == 1:
    print(mode[0])
else:
    mode.sort()
    print(mode[1])

#범위
sys.stdout.write(str(max(arr)-min(arr)) + '\n')
