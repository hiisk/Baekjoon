import sys
import math
T = int(input())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(int(A*B/math.gcd(A,B)))