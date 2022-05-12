import sys
N = sys.stdin.readline()
N_array = set(sys.stdin.readline().split())
M = sys.stdin.readline()
M_array = sys.stdin.readline().split()

for i in M_array:
    sys.stdout.write('1\n') if i in N_array else sys.stdout.write('0\n')