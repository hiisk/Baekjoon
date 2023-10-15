import sys
input = sys.stdin.readline
N = int(input())
start = 1
end = 1
sum = 1
count = 1 

if N == 1 or N == 2:
  print(1)
  sys.exit()

while end < N//2 + 2:
  if sum == N:
    count += 1
    end += 1
    sum += end
  elif sum < N:
    end += 1
    sum += end
  else:
    sum -= start
    start += 1
print(count)