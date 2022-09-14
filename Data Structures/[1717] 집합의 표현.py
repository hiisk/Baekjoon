import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []

for _ in range(m):
    check = True
    num, a, b = map(int, input().split())
    if num == 0:
        if not arr:
            arr.append([a,b])
            continue
        for x in range(len(arr)):
            if a in arr[x]:
                arr[x] = arr[x] + [b]
                check = False
                break
            elif b in arr[x]:
                arr[x] = arr[x] + [a]
                check = False
                break
        if check:
            arr.append([a,b])
    elif num == 1:
        for x in arr:
            if a in x and b in x:
                if a == b:
                    if x.count(a) != 2:
                        break
                print("YES")
                check = False
                break
        if check:
            print("NO")
# ========================================
import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    num, a, b = map(int, input().split())
    if num == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")