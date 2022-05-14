import sys
from collections import Counter

_ = int(input())
N_array = list(input().split())
_ = int(input())
M_array = list(input().split())
dic = Counter(N_array)

print(' '.join(f'{dic[i]}' if i in dic else '0' for i in M_array))
