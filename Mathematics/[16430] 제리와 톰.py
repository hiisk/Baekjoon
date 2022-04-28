from math import gcd 
A, B = map(int, input().split())
print((B-A)//gcd(B-A,B), B//gcd(B-A,B))