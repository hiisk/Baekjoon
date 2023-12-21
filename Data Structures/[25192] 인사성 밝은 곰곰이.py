import sys
input = sys.stdin.readline

n = int(input())
set_arr = set()
cnt = 0

for _ in range(n):
    user = input().strip()
    if user == 'ENTER':
        cnt += len(set_arr)
        set_arr = set()
    else:
        set_arr.add(user)

cnt += len(set_arr)
print(cnt)