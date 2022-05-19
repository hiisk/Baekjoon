import sys
tmp = sys.stdin.readline()

arr = []

for i in range(len(tmp)-1):
    arr.append(tmp[i:].strip("\n"))

print(*sorted(arr), sep="\n")