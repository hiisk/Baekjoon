import sys

n = int(sys.stdin.readline().rstrip())
arr = set()

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()

    if b == "enter":
        arr.add(a)
    elif b == "leave":
        arr.discard(a)
print(*sorted(arr, reverse=True), sep="\n")