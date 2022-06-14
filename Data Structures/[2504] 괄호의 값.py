arr = input()
stack = []

for i in arr:
    if not stack:
        if i in [')', ']']:
            print(0)
            exit(0)
            
    if i == ')':
        tmp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                if tmp == 0:
                    stack.append(2)
                else:
                    stack.append(tmp*2)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                tmp += int(top)
        
    elif i == ']':
        tmp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(tmp*3)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                tmp += int(top)
                
    else:
        stack.append(i)

try:
    print(sum(stack))
except:
    print(0)