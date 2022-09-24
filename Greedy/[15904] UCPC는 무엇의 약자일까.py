inp = input()
check = ""
arr = ["U","C","P","C"]

for i in inp:
    if i == arr[len(check)]:
        check +=arr[len(check)]
        if len(check) == 4:
            print("I love UCPC")
            exit()
print("I hate UCPC")