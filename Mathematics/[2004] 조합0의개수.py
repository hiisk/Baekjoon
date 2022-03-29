n, m = map(int, input().split())

n_2 = 0
n_5 = 0

for i in range(1, n):
    if i == m+1:
        print(min(n_2,n_5))
        break
    while True:
        tmp = n-i+1
        if tmp/2 == tmp//2:
            while True:
                tmp = tmp//2
                n_2 += 1
                if tmp % 2 != 0:
                    break
        if tmp/5 == tmp//5:
          while True:
                tmp = tmp//5
                n_5 += 1
                if tmp % 5 != 0:
                    break
        break
    while True:
        tmp = i
        if tmp/2 == tmp//2:
            while True:
                tmp = tmp//2
                n_2 -= 1
                if tmp % 2 != 0:
                    break
        if tmp/5 == tmp//5:
          while True:
                tmp = tmp//5
                n_5 -= 1
                if tmp % 5 != 0:
                    break
        break


n, m = map(int, input().split())

def combi(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

n_2 = combi(n, 2) - combi(m, 2) - combi(n - m, 2)
n_5 = combi(n, 5) - combi(m, 5) - combi(n - m, 5)

print(min(n_2, n_5))