import sys
input = sys.stdin.readline
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x, y = map(int, input().split())
tmp = 0

for i in range(x-1):
    tmp += month[i]
tmp+=y

print(week[tmp%7])