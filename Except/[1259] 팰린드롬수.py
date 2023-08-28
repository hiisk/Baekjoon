while 1:
    tmp = input()
    if tmp == "0":
        break
    elif tmp == tmp[::-1]:
        print("yes")
    else:
        print("no")