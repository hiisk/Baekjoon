num = int(input())

for i in range(num):
    a, b, x, c ,d, y = map(int, input().split())
    if ((a == c and b == d) or (a==d and b == c)) and x!=y or a**2 + d**2 > x**2 + y**2 or b**2 + c**2 > x**2 + y**2:
        print("0")
    elif a == c and b == d and x==y:
        print("-1")    
    elif (abs(a-c) == x+y or abs(b-d) == x+y or abs(a-d) == x+y or abs(b-c) == x+y):
        print("1")
    else:
        print("2")
    
import math
n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance == 0 and r1 == r2 :
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:
        print(1)
    elif abs(r1-r2) < distance < (r1+r2) :
        print(2)
    else:
        print(0)