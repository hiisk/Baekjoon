N = int(input())
arr = list(input())

print(min((N - arr.count("S"))//2 + arr.count("S") + 1, N))