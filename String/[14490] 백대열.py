import math
n,m = map(int,input().split(":"))

print(f"{n//math.gcd(n,m)}:{m//math.gcd(n,m)}")