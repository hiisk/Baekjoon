E, S, M = map(int, input().split())

if E == S and S == M:
    print(E)
else:
    while True:
        if E == S and S == M:
            print(E)
            break
        E += 15
        if E > S:
            S += 28
        if E > M:
            M += 19
        
