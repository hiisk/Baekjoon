from math import gcd
a, b = map(int, input().split())
c, d = map(int, input().split())

ja = a*d + b*c
mo = b*d

tmp = gcd(ja,mo)

print(f'{ja//tmp} {mo//tmp}')
