n = int(input())
m = list(input())
alpha = [0] * n

for i in range(n):
    alpha[i] = int(input())
stack = []

for s in m:

    if s.isalpha():
        stack.append(alpha[ord(s) - ord('A')])
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if s == '+' :
            stack.append(n1+n2)
        elif s == '-':
            stack.append(n1-n2)
        elif s == '*':
            stack.append(n1*n2)
        elif s == '/':
            stack.append(n1/n2)

print(f'{stack[0]:.2f}')